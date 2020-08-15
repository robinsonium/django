from django.db import models
import re


class UserManager(models.Manager):
    def validate_reg(self, postdata):
        errors = {}
        
        # NAMES MUST BE LONGER THAN 2 CHARACTERS
        if len(postdata['first_name']) < 2:
            errors['first_name_length'] = "First name must be at least 2 characters"
        if len(postdata['last_name']) < 2:
            errors['last_name_length'] = "Last name must be at least 2 characters"

        # EMAIL IS A VALID REGEX
        email_pattern = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_pattern.match(postdata['email']):
            errors['email_pattern'] = "Invalid email address"

        # EMAIL MUST BE UNIQUE
        all_users = User.objects.all()
        emails = [x.email for x in all_users]
        if postdata['email'] in emails:
            errors['unique_email'] = "This email is already registered"        

        # PASSWORD MUST MATCH CONFIRMATION
        passwd = postdata['password']
        passwd_conf = postdata['confirmation']
        if passwd != passwd_conf:
            errors['confirmation'] = "Password did not match confirmation"

        # PASSWORD MUST BE AT LEAST 8 CHARACTERS
        if len(passwd) < 8:
            errors['pwlength'] = "Password must be at least 8 characters"

        # PASSWORD NEEDS AT LEAST 1 UPPERCASE CHARACTER
        if not any(n.isupper() for n in passwd):
            errors['uppercase'] = "Password must have at least one upper case character"
        return errors

    ## logins have different post data, hence a different validator
    def validate_login(self,postdata):
        errors={}
        # EMAIL IS A VALID REGEX
        email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_pattern.match(postdata['email']):
            errors['email_pattern'] = "Invalid email address"
        return errors

     ## edits have different post data, hence a different validator
    def validate_edit(self,postdata):
        errors={}
        # NAMES MUST BE LONGER THAN 2 CHARACTERS
        if len(postdata['first_name']) < 2:
            errors['first_name_length'] = "First name must be at least 2 characters"
        if len(postdata['last_name']) < 2:
            errors['last_name_length'] = "Last name must be at least 2 characters"
        # EMAIL IS A VALID REGEX

        email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_pattern.match(postdata['email']):
            errors['email_pattern'] = "Invalid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class QuoteManager(models.Manager):
    def validate(self, postdata):
        errors = {}
        if len(postdata['content']) < 10:
            errors['quote_length'] = "Quotes must be 10 characters or longer"
        if len(postdata['author']) < 3:
            errors['author'] = "Author's name must be at least 3 characters"
        return errors


class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, related_name="quotes", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,related_name="likes",)
    objects = QuoteManager()
