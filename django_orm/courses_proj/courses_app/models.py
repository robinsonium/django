from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import pytz
from pytz import timezone

class CourseManager(models.Manager):
    def validate(self, postdata):
        errors = {}
        
        if len(postdata['course_name']) < 5:
            errors['length_name']="Name must be at least 5 characters. Anything less would be horrible, and useless. I shouldn't even have to say this to you.¸"    
            # print("error with course_name being too short")
        
        # Validate description
        if len(postdata['course_description']) < 15:
            errors['description']="'Description' must be at least 15 characters"
            # print("error with description being too short")
        print(errors)
        return(errors)


class Description(models.Model):
    content=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    description=models.ForeignKey(Description,related_name="course",on_delete=models.CASCADE, null=True)
    objects=CourseManager()

class Comment(models.Model):
    content=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    course=models.ForeignKey(Course,related_name="comment",on_delete=models.CASCADE,null=True)



    

