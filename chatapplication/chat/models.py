from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, default=1)
    def __str__(self):
        return 'プロフィールID' + str(self.id) + '名前' + self.name + '年齢' + str(self.age) + 'ユーザーID' + str(self.user)

class Room(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return 'ルームID' + str(self.id) + 'プロフィールID' +str(self.profile.id) + 'ユーザーID' +str(self.user.id)
