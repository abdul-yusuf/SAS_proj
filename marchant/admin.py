from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Reviews)
admin.site.register(models.Rating)
admin.site.register(models.Images)

