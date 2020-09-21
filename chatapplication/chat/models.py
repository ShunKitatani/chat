from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + self.name + str(self.age)
