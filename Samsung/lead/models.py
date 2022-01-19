import email
from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length=300, default='enny')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, default='17 Ikoyi')
    email = models.EmailField(max_length=300, default='eniolaakinpelu6@gmail.com')
    age = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.email} ......{self.user.name}'


class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null=True)
    address = models.CharField(max_length=300, default='15 Ikoyi')
    email = models.CharField(max_length= 200, default='eniola@gmail.com')
    age = models.IntegerField(default=3)

    def __str__(self):
        return f'{self.email} .....'

