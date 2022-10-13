from email.policy import default
from itertools import product
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
    sub_product = models.ManyToManyField('SubProduct', blank=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    images = models.ManyToManyField('Images', blank=True)
    rating = models.OneToOneField('Rating', on_delete=models.AutoField, blank=False, null=True)
    
    rate = [2,3,42,53,5]
    @property
    def rate(self):
        ratex = self.rating
        summ = ratex.rate1+ratex.rate2*2+ratex.rate3*3+ratex.rate4*4+ratex.rate5*5
        sumz = ratex.rate1+ratex.rate2+ratex.rate3+ratex.rate4+ratex.rate5
        rates = summ/sumz
        return int(rates)

    def __str__(self) -> str:
        return self.title

class Rating(models.Model):
    """
    Rating System on a Scale of (5)
    """
    rate1 = models.IntegerField(default=0)
    rate2 = models.IntegerField(default=0)
    rate3 = models.IntegerField(default=0)
    rate4 = models.IntegerField(default=0)
    rate5 = models.IntegerField(default=0)

class SubProduct(models.Model):
    """
    A sub category of product i.e room1, room2, room3 of product1
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    images = models.ManyToManyField('Images', blank=True)
    rating = models.OneToOneField('Rating', on_delete=models.AutoField, blank=False, null=True)
    
    @property
    def rate(self):
        ratex = self.rating
        summ = ratex.rate1+ratex.rate2*2+ratex.rate3*3+ratex.rate4*4+ratex.rate5*5
        sumz = ratex.rate1+ratex.rate2+ratex.rate3+ratex.rate4+ratex.rate5
        rates = summ/sumz
        return int(rates)

    def __str__(self):
        return self.title

class Images(models.Model):
    pass
    # image = models.ImageField()

class Review(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    reply = models.ForeignKey('ReviewReply', on_delete=models.CASCADE, blank=True, null=True)

class ReviewReply(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
