from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    password=models.CharField(max_length=225)
    username=models.CharField(max_length=225,unique=True)
    role=models.ForeignKey(Role,on_delete=models.SET_NULL,null=True)
    last_login=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    access_token=models.CharField(max_length=725,null=True,blank=True)

    def get_role_name(self):
        return self.role.name if self.role.name else None

class UserProfile(models.Model):
    username=models.CharField(max_length=225,unique=True)
    role_name=models.CharField(max_length=50,null= True, blank=True)