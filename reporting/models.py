from django.db import models

# Create your models here.

class Order(models.Model):

    amount = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_time = models.DateTimeField()