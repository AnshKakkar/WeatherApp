from django.db import models
from Login_Api.models import Account
from django.contrib.auth.models import User
# Create your models here.
class Preference(models.Model):
    city_name=models.CharField(max_length=50, default=None)
    account=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
        return self.city_name