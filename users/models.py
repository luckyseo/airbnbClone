from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(default="")  # isgonna showup in admin page
    pass
