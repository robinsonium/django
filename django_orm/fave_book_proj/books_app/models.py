from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def validate(self, postdata):
        errors={}
        if len(postdata['title']) == None:
            errors['length']="Title is required"
        if len(postdata['description'])<5:
            errors['desc']="Description must be at least 5 characters"
        return errors

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uploaded_by=models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE,null=False)
    users_who_like=models.ManyToManyField(User, related_name="liked_books", null=True)
    objects=BookManager()
