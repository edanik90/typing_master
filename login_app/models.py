from django.db import models
import re

class UserManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) <= 0:
            errors['first_name'] = "First name required!"
        if len(post_data['first_name']) > 55:
            errors['first_name'] = "First name can not exceed 55 characters"
        if len(post_data['last_name']) <= 0:
            errors['last_name'] = "Last name required!"
        if len(post_data['last_name']) > 55:
            errors['last_name'] = "Last name can not exceed 55 characters"
        try: 
            User.objects.get(email = post_data['email'])
            errors['email'] = "This email address is already in use"
        except:
            pass
        alias_list = User.objects.filter(alias = post_data['username'])
        if len(alias_list) != 0:
            errors['alias_taken'] = "Provided username is already in use"
        if len(post_data['username']) < 6:
            errors['alias_taken'] = "Username is required; it should be between 6 and 55 characters long"
        if len(post_data['username']) > 55:
            errors['alias_taken'] = "Username can not exceed 55 characters"
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['invalid_email'] = "Invalid email address!"
        if len(post_data['email']) > 384:
            errors['email'] = "Email cannot be longer than 384 characters!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters long!"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords don't match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    alias = models.CharField(max_length = 55)
    email = models.CharField(max_length = 384)
    password = models.CharField(max_length = 60)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def top_speed(self):
        return self.taken_tests.all().order_by("-speed").first()
    
    def top_accuracy(self):
        return self.taken_tests.all().order_by("-accuracy").first()