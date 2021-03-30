from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
    # Create your models here.

class profile(AbstractBaseUser):
    first_name =  models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    address = models.TextField(max_length=255, null =True)
    phone = models.TextField(max_length=11, unique=True)

   ## USERNAME_FIELD = 'email'
    ##REQUIRED_FIELD = []
