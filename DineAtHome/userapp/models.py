from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'Admin'
    CHEF = 'Chef'
    CUSTOMER = 'Customer'
    
    phone = models.BigIntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    role = models.CharField(max_length=255,null=True,blank=True,default=CUSTOMER)