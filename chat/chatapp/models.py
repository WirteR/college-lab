from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    message = models.TextField(max_length=256)
    date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
