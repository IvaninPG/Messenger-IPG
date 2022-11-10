from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    nameMember = models.OneToOneField(User, on_delete=models.CASCADE)
    avatarMember = models.ImageField()

class Room(models.Model):

