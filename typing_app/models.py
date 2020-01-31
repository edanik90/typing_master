from django.db import models
from login_app.models import User

class TextManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['content']) <= 0:
            errors['content'] = "Text is required!"
        return errors

class Text(models.Model):
    content = models.TextField()
    difficulty = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TextManager()

class Test(models.Model):
    speed = models.FloatField()
    errors = models.PositiveSmallIntegerField()
    accuracy = models.FloatField()
    user = models.ForeignKey(User, related_name = "taken_tests", on_delete = models.CASCADE)
    text = models.ForeignKey(Text, related_name = "used_texts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)