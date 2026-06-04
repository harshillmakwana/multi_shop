from django.contrib import admin
from appmodule.multishop_adminapp import models

# Register your models here.

admin.site.register(models.category),
admin.site.register(models.category_sbu),
admin.site.register(models.category_sub_sub),
admin.site.register(models.product),