from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import pytz
from pytz import timezone

# class ShowManager(models.Manager):
#     def validate_show(self, postdata):
#         errors = {}
        
#         # Validate title
#         all_shows=Show.objects.all()
#         titles=[x.title for x in all_shows]
#         if postdata['title'] in titles:
#             errors['title']: "Title must be unique. We already have this one"
        
#         if len(postdata['title']) < 2:
#             if 'title' in errors.keys():
#                 errors['title'] = errors['title']+" and titles must have at least 2 characters, otherwise that's a terrible title. Even '24' had two characters"
#             errors['title']="Titles must have at least 2 characters, otherwise that's a terrible title. Even '24' had two characters"
        
#         # Validate network
#         if len(postdata['network']) < 3:
#             errors['network'] = "Network should have at least 2 characters. I can't think of any networks with less than 2. Come on, man"
        
#         # Validate release date
#         pacific=timezone('US/Pacific')
#         release_date_obj=datetime.strptime(postdata['release_date'],"%Y-%m-%d")
#         rel_date=release_date_obj.astimezone(pacific).strftime("%Y-%m-%d")
#         now=datetime.now().astimezone(pacific).strftime("%Y-%m-%d")
#         if  rel_date > now:
#             errors['release_date'] = "Release date cannot be in the future. That's a chump move"
        
#         # Validate description
#         if len(postdata['description']) > 0 and len(postdata['description']) < 10:
#             errors['description'] = "'Description' is optional, but if provided, it must be at least 10 characters"
#         return(errors)

# Create your models here.

class Description(models.Model):
    content=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    description=models.ForeignKey(Description,related_name="course",on_delete=models.CASCADE)

