from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new-post", views.new_post, name="new_post"),
    path("like/<int:post_id>", views.like_post, name="like-post"),
    path("user/<int:user_id>/page/<int:page_no>", views.view_user, name="user-posts"),
    path("edit/<int:post_id>", views.edit_post, name="edit-post"),
    path("page/<int:page_no>", views.page_load, name="page"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path("post/<int:post_id>/comment", views.add_comment, name="add-comment"),
    path('view-post/<int:post_id>/', views.view_post, name='view-post'),
    path("marketplace", views.marketplace, name = "marketplace"),
    path("chat", views.chat, name = "chat"),
    path("edit-comment/<int:comment_id>/", views.edit_comment, name="edit-comment"),
    path("delete-comment/<int:comment_id>/", views.delete_comment, name="delete-comment"),
]
