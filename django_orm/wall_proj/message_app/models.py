from django.db import models
from login_app.models import User

# Create your models here.
class Message(models.Model):
    content=models.TextField()
    poster=models.ForeignKey(User,related_name="message",on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content=models.TextField()
    poster=models.ForeignKey(User,related_name="comment",on_delete=models.CASCADE, null=True)
    message=models.ForeignKey(Message,related_name="comment",on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
