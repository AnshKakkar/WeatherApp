from django.db import models


class Account(models.Model):
    username=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=100, default=None, null=True, blank=True)
    password=models.CharField(max_length=100, default=None, null=True)

# Create your models here.
# class Preference(models.Model):
#     username=models.CharField(max_length=50)
#     city_p1=models.CharField(max_length=50)
#     city_p2=models.CharField(max_length=50)
#     city_p3=models.CharField(max_length=50)


    def __str__(self):
        return self.username