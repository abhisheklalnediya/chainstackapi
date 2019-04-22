from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    quota = models.IntegerField(default = -1) # -1 = unlimited

class QuotaCredit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.IntegerField()


def set_quota(sender, instance, created, **kwargs):
    if created:
        instance.user.quota = instance.user.quota + instance.credit if instance.user.quota != -1 else instance.credit
        instance.user.save()

post_save.connect(set_quota, sender=QuotaCredit)