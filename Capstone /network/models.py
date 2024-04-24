from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Posts(models.Model):
    content = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    like = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)  # Add title field
    description = models.CharField(max_length=255)  # Add description field
    imageUrl = models.URLField(max_length=1000)  # Add imageUrl field
    def __str__(self):
        return f"{self.user}: {self.content} @{self.time}. Likes: {self.like}"


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post} at {self.created_at}"

class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="liked_usr")
    liked_users = models.ManyToManyField(User, blank=True, related_name="liked_posts")

