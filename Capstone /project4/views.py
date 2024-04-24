import json
import logging
from django import http
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.utils import ProgrammingError
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

from .models import User, Posts, Like ,Comment

def liked_list(posts, user):
    liked_posts = []
    for post in posts:
        for p in post.liked_usr.all():
            for usr in p.liked_users.all():
                if usr == user:
                    liked_posts.append(post.id)
    return liked_posts




def get_page(page_id):
    posts = Posts.objects.all().order_by('-time')
    return Paginator(posts, 10).page(page_id)


def blog(request):
    # Fetch posts
    posts = Posts.objects.all().order_by('-time')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get the IDs of posts liked by the current user
    liked_posts = liked_list(posts, request.user)
    
    return render(request, "network/blog.html", {
        "posts": page_obj,
        "liked_posts": liked_posts,
        "pages": "page",
        "title": [post.title for post in page_obj],
        "description": [post.description for post in page_obj],
        "imageUrl": [post.imageUrl for post in page_obj],  
        "content" :[post.content for post in page_obj]
    })
    
def index(request):
       return render(request, "network/index.html")
   
def about(request):
    return render(request, "network/about.html")

def chat(request):
    return render(request, "network/chat.html")

def marketplace(request):
    return render(request, "network/marketplace.html")   

@csrf_exempt
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    
def new_post(request):
    if request.method == "POST":
        # Check if the required fields are present in the form data
        title = request.POST.get("title")
        description = request.POST.get("description")
        imageUrl = request.POST.get("imageUrl")
        
        if title and description and imageUrl:
            # Create a new post with the submitted data
            post = Posts(user=request.user, title=title, description=description, imageUrl=imageUrl)
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            # If any required field is missing, return an error response
            return HttpResponse("Missing required fields in the form data", status=400)
    else:
        # Render the create post form template
        return render(request, "network/create.html")


@csrf_exempt
def like_post(request, post_id):
    if request.method == "POST":
        try:
            post = Posts.objects.get(pk=post_id)
        except:
            return JsonResponse({"stat": "failed"}, status=404)
        
        try:
            l = Like.objects.filter(post=post).first()
            l = l.liked_users
        except:
            Like(post=post).save()
            l = Like.objects.filter(post=post).first()
            l = l.liked_users
        for usr in l.all():
            if request.user == usr:
                l.remove(request.user)
                post.like = l.count()
                post.save()
                return JsonResponse({"stat": "Success", "likes": l.count(), "action": "u"}, status=200)
            
        l.add(request.user)
        post.like = l.count()
        post.save()
        
        return JsonResponse({"stat": "Success", "likes": l.count(), "action": "l"}, status=200)
    
    return HttpResponse("This page only accepts Post requests")

@csrf_exempt
def view_user(request, user_id, page_no):
    usr_ = User.objects.get(pk=user_id)
    
    try:
        follow_data = usr_.follows.first()
        followers = follow_data.followers.all()
        followings = follow_data.followed_users.all()
        f = "Follow" if request.user not in followers else "Unfollow"
    except AttributeError:  # Handle the case where follows is None
        followers = []
        followings = []
        f = "Follow"
    
    posts = usr_.user_posts.all().order_by("-time")
    posts = Paginator(posts, 10).page(page_no)
    liked_posts = liked_list(posts, request.user)
    
    return render(request, "network/user.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "usr": usr_,
        "followers": len(followers),
        "followings": len(followings),
        "btnText": f
    })


def view_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'network/post.html', {'post': post})    


    
@csrf_exempt
def add_comment(request, post_id):
    if request.method == "POST":
        # Retrieve the current user
        current_user = request.user
        
        # Retrieve the post object
        post = get_object_or_404(Posts, pk=post_id)
        
        # Retrieve the comment message from the POST data
        message = request.POST.get('newComment')

        # Create a new comment object
        new_comment = Comment(
            author=current_user,
            message=message,
            post=post  # Associate comment with the post
        )
        new_comment.save()

        # Redirect back to the view_post page
        return redirect('view-post', post_id=post_id)
    
    # Return an error response for other HTTP methods
    return JsonResponse({"error": "This endpoint only accepts POST requests"}, status=405)

@csrf_exempt
def edit_comment(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.author == request.user:
            message = json.loads(request.body).get("message")
            comment.message = message
            comment.save()
            return JsonResponse({"success": True, "message": "Comment edited successfully"})
        else:
            return JsonResponse({"success": False, "message": "You are not authorized to edit this comment"})
    else:
        return HttpResponseNotAllowed(["POST"])
    

@csrf_exempt
def edit_post(request, post_id):
    if request.method == "POST":
        post = Posts.objects.get(pk=post_id)
        if post.user == request.user:
            data = json.loads(request.body).get("edited")
            post.content = data
            post.save()
            return JsonResponse({"stat": "Success", "content": data}, status=200)
        else:
            return JsonResponse({"stat": "Failed"}, status=404)
    else:
        return HttpResponse("Try harder")

@csrf_exempt
def delete_comment(request, comment_id):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.author == request.user:
            post = comment.post
            comment.delete()
            return JsonResponse({"success": True, "message": "Comment deleted successfully"})
        else:
            return JsonResponse({"success": False, "message": "You are not authorized to delete this comment"})
    else:
        return HttpResponseNotAllowed(["DELETE"])



def page_load(request, page_no):
    posts = get_page(page_no)
    liked_posts = liked_list(posts, request.user)
    return render(request, "network/blog.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "pages": "page"
    })
        