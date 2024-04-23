from django.contrib import admin
from .models import  User, Posts, Like, Follower

class PostsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content", "time", "like")

# Register your models here.
admin.site.register(User)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Like)
admin.site.register(Follower)