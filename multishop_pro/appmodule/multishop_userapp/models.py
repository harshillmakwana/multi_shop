from django.db import models
from django.contrib.auth.models import AbstractUser
from appmodule.multishop_adminapp.models import product


# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICE = (
        ('Admin','Admin'),
        ('User','User'),
    )
    email = models.EmailField(max_length=254,unique=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=250,null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICE, max_length=50,default='User')
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    city = models.CharField(null=True,blank=True, max_length=50)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.email} ({self.role})"
    

class wishlist(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pro_name = models.ForeignKey(product, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)


class add_to_card(models.Model):
    pro_name = models.CharField(max_length=50)
    product_image = models.FileField(upload_to='add_to_card',null=True,blank=True)
    pro_price = models.IntegerField()
    # pro_quatity = models.IntegerField()
    # total_price = models.IntegerField()
    

class address(models.Model):
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField() 
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    
      
    
class payment(models.Model):
    number = models.IntegerField()
    cvv = models.IntegerField()
        

class RazorpayPayment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    signature = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Success')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"

# -------------------------------------------------------------------------
# 📦 Order & OrderItem – models for purchase history
# -------------------------------------------------------------------------
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)  # Razorpay order ID
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(RazorpayPayment, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='orders')

    def __str__(self):
        return f"Order {self.order_id} – {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('multishop_adminapp.product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}× {self.product.product_name}"
