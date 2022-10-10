from turtle import title
from django.db import models

# Create your models here.

CATEGORIES = (
    ('R', 'Rent'),
    ('S', 'Sell'),
)

TIMEFRAME = (
    ('L', 'Lifetime'),
    ('M', 'Monthly'),
    ('Y', 'Yearly')
)

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORIES, max_length=1, default='R')
    timeframe = models.CharField(choices=TIMEFRAME, max_length=1, default='Y')
    sub_product = models.ManyToManyField('Sub_Product', blank=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    images = models.ManyToManyField('Images', blank=True)
    def __str__(self) -> str:
        return self.title

class Sub_Product(models.Model):
    """
    A sub category of product i.e room1, room2, room3 of product1
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    images = models.ManyToManyField('Images', blank=True)

class Images(models.Model):
    pass
    # image = models.ImageField()