from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Signup(models.Model):
    user = models.CharField (max_length=200)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=300,primary_key=True, null=False)
    image = models.FileField(null=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.user

class Login(models.Model):
    uname = models.CharField(max_length=200)
    password = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.uname

class Orders(models.Model):
    rname = models.CharField(max_length=200, null=True)
    rmail = models.CharField(max_length=200, null=True)
    rphone = models.CharField(max_length=200, null=True)
    rorder = models.CharField(max_length=200, null=True)
    rdate = models.CharField(max_length=200, null=True)
    rsid = models.CharField(max_length=200, null=True)
    rsidno = models.CharField(max_length=200, null=True)
    rweight = models.CharField(max_length=200, null=True)
    raddress = models.CharField(max_length=200, null=True)
    rstatus = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.rname