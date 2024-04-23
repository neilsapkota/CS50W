
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new-post", views.new_post, name="new-post"),
    path("following/<int:page_id>", views.follow_view, name="following"),
    path("like/<int:post_id>", views.like_post, name="like-post"),
    path("user/<int:user_id>/page/<int:page_no>", views.view_user, name="user-posts"),
    path("edit/<int:post_id>", views.edit_post, name="edit-post"),
    path("page/<int:page_no>", views.page_load, name="page"),
]