from distutils.command.upload import upload
import profile
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    def __str__(self):
        return str(self.username)



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='user/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
    