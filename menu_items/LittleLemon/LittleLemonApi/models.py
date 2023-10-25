from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()