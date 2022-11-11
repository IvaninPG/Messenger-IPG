from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    nameMember = models.OneToOneField(User, on_delete=models.CASCADE)
    avatarMember = models.ImageField()

class Room(models.Model):
    memberRoom = models.ForeignKey(Member, on_delete=models.CASCADE)
    nameRoom = models.CharField(max_length=128)
    textRoom = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)



