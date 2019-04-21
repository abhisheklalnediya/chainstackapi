from django.db import models
from User.models import User
# Create your models here.


class Care (models.Model):
    name = models.CharField(max_length = 20)
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
