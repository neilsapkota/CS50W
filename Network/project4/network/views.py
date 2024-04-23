import json
from django import http
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.utils import ProgrammingError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Posts, Like , Follower

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


def index(request):
    posts = get_page(1)
    liked_posts = liked_list(posts, request.user)
    return render(request, "network/index.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "pages": "page"
    })


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
            user_f = Follower(user=user)
            user_f.save()
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
        post = Posts(user=request.user, content=request.POST["content"])
        post.save()
        return HttpResponseRedirect(reverse('index'))
    
    return HttpResponse("Error: This page only accepts post requests")

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
    if request.method == "POST":
        usr_followed = User.objects.get(pk=user_id)
        usr_following = request.user
        follow_data = usr_followed.follows.first()

        if usr_following in follow_data.followers.all():
            follow_data.followers.remove(usr_following)
            usr_following.follows.first().followed_users.remove(usr_followed)
            return JsonResponse({
            "stat": "Follow",
            "followers": follow_data.followers.all().count(),
             "following": follow_data.followed_users.all().count()}, status=200)
        else:
            follow_data.followers.add(usr_following)
            usr_following.follows.first().followed_users.add(usr_followed)
            return JsonResponse({
            "stat": "Unfollow", 
            "followers": follow_data.followers.all().count(),
            "following": follow_data.followed_users.all().count()}, status=200)

    
    usr_ = User.objects.get(pk=user_id)
    posts = usr_.user_posts.all().order_by("-time")
    posts = Paginator(posts, 10).page(page_no)
    liked_posts = liked_list(posts, request.user)
    followers = usr_.follows.first().followers.all()
    
    f = "Follow"
    if request.user in followers:
        f = "Unfollow"
    followings = usr_.follows.first().followed_users.all()
    
    return render(request, "network/user.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "usr": usr_,
        "followers": len(followers),
        "followings": len(followings),
        "btnText": f
        
    })


def follow_view(request, page_id):
    followed_usr = Follower.objects.get(user=request.user).followed_users.all()
    posts = Posts.objects.filter(user__in=followed_usr)
    posts = Paginator(posts, 10).page(page_id)
    liked_posts = liked_list(posts, request.user)

    return render(request, "network/index.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "pages": "following"
    })


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
    
def page_load(request, page_no):
    posts = get_page(page_no)
    liked_posts = liked_list(posts, request.user)
    return render(request, "network/index.html", {
        "posts": posts,
        "liked_posts": liked_posts,
        "pages": "page"
    })
    