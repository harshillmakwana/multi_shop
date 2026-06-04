from django.contrib import admin
from appmodule.multishop_userapp import models

# Register your models here.


admin.site.register(models.add_to_card),
admin.site.register(models.CustomUser),
admin.site.register(models.address),
admin.site.register(models.payment)
admin.site.register(models.RazorpayPayment)