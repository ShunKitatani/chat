from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + self.name + str(self.age)

# class Room(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     content = models.CharField(max_length=100)
#     pub_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.id) + self.content + str(self.pub_date)
