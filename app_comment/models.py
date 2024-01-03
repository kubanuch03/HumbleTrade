from django.db import models
from app_blog.models import Post

from django.utils import timezone
from app_clients.models import Client
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField() 
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"