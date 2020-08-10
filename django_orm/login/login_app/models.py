from django.db import models
from datetime import datetime
import pytz
from pytz import timezone
from dateutil.relativedelta import relativedelta


class UserManager(models.Manager):
    def validate(self,postdata):
        errors={}
        
        # NAMES MUST BE LONGER THAN 2 CHARACTERS
        if len(postdata['first_name']) < 3:
            errors['first_name_length']="First name must be longer than 2 characters"
        if len(postdata['last_name']) < 3:
            errors['last_name_length']="First name must be longer than 2 characters"
        
        # EMAIL MUST BE UNIQUE
        all_users=User.objects.all()
        emails=[x.email for x in all_users]
        if postdata['email'] in emails:
            errors['unique_email']="This email is already registered"
        
        # BIRTHDAY MUST BE IN THE PAST
        pacific=timezone('US/Pacific')
        birthday_obj=datetime.strptime(postdata['birthday'],"%Y-%m-%d")
        birthday_date=birthday_obj.astimezone(pacific).strftime("%Y-%m-%d")
        now=datetime.now().astimezone(pacific).strftime("%Y-%m-%d")
        if birthday_date > now:
            errors['birthday_in_past'] = "Birthday cannot be in the future. That's crazy talk"
        
        # BIRTHDAY MUST BE 13+ YEARS AGO
        if birthday_obj + relativedelta(years=13) > datetime.now():
            errors['age_limit']="You must be at least 13 years old"

        # USER MUST BE 13 YEARS OLD OR MORE
        # 13 years ago today = datetime.now()+relativedelta(years=-13)
        # user['dateOfBirth'] + dateutil.relativedelta.relativedelta(years=18) > datetime.date.today()
        # bday=datetime.strptime("2005-06-01","%Y-%m-%d") <-- get user's birthday as datetime object
        # bday + dateutil.relativedelta.relativedelta(years=13) > datetime.now()

        
# email is a valid regex

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    birthday=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
