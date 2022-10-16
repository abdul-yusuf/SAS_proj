from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Payment)
admin.site.register(models.Coupon)
admin.site.register(models.Viewed)
admin.site.register(models.BookMarked)