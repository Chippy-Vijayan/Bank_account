from django.db import models

# Create your models here.
class register(models.Model):
    first_name = models.CharField(max_length=250,primary_key=True)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.f_name
class branches(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField()
    sub_branc = models.CharField(max_length=250)
    def __str__(self):
        return self.name