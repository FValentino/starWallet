from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    cuil = models.CharField(null=False, max_length=11, unique=True)
    tel = models.CharField(null=False, max_length=15)
    birthdate = models.DateField(null=False)
    balance = models.DecimalField(null=False, default=0, decimal_places=2, max_digits=12)
    perfil_pic = models.ImageField(null=True, upload_to='profile_pics/', blank=True)
