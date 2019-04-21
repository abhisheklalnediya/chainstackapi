from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    quota = models.IntegerField(default = -1) # -1 = unlimited

class QuotaCredit(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    credit = models.IntegerField