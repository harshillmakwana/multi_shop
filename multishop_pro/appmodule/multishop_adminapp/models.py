from django.db import models

# Create your models here.

#admin
# category1 = man , woman , kids , electronic
# category2 = man -> watch ,cloth
# category3 = man -> watch -> analog or sport
# peoduct = watch , cloth , footware , camera

# user 
# User/admin = regisration and login
# add to card or like optinal
# address = user
# payment  = user
# order = user 
# feedback by user  

class category(models.Model):
    category_name1 = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    is_action = models.BooleanField(default=True) 
    
class category_sbu(models.Model):
    category_main = models.ForeignKey(category, on_delete=models.CASCADE)
    category_name2 = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    is_action = models.BooleanField(default=True)
    cat_image = models.FileField(upload_to='category_sbu/')
    
class category_sub_sub(models.Model):
    cate_one = models.ForeignKey(category, on_delete=models.CASCADE)
    cate_two =models.ForeignKey(category_sbu, on_delete=models.CASCADE) 
    category_name3 = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    is_action = models.BooleanField(default=True)
    
class product(models.Model):
    cate_one = models.ForeignKey(category, on_delete=models.CASCADE)
    cate_two =models.ForeignKey(category_sbu, on_delete=models.CASCADE)
    cate_three =models.ForeignKey(category_sub_sub, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50,null=True,blank=True)
    product_image = models.FileField(upload_to='product/')
    product_price = models.IntegerField()
    descount_price = models.IntegerField()
    product_despcrition = models.TextField()
    brand = models.CharField(max_length=100)
    stock = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    
    @property
    def name(self):
        return self.product_name
    
    @property
    def price(self):
        return float(self.descount_price)
    
    @property
    def image(self):
        return self.product_image.url
    
    
    def __str__(self):
        return self.product_name