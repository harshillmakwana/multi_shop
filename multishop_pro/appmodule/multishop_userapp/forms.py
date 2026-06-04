from django import forms
from appmodule.multishop_userapp import models

class add_to_card_form(forms.ModelForm):
    class Meta:
        model = models.add_to_card
        fields = '__all__'
        
class ragister_form(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ['username','email','phone_number','first_name','city','password']
        
class wishlist_form(forms.ModelForm):
    class Meta:
        model = models.wishlist
        fields = '__all__'
        
class address_form(forms.ModelForm):
    class Meta:
        model = models.address
        fields = '__all__'
        
class payment_form(forms.ModelForm):
    class Meta:
        model = models.payment
        fields = '__all__'
        