from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, default=1)

    def __str__(self):
        return str(self.id) + self.name + str(self.age) + ',' + str(self.user)
