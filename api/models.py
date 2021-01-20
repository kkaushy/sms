from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    name = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=32,blank=True, null=True) 


class SMS(models.Model):
    text = models.TextField()
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name="sender", null=False)
    reciever = models.ForeignKey('User', on_delete=models.CASCADE, related_name="reciever", null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
