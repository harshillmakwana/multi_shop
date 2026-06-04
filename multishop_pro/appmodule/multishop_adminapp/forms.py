from django import forms
from appmodule.multishop_adminapp import models

class category_form(forms.ModelForm):
    class Meta:
        model = models.category
        fields = '__all__'
        
class category_sub_form(forms.ModelForm):
    class Meta:
        model = models.category_sbu
        fields = '__all__'
        
class category_sub_sub_form(forms.ModelForm):
    class Meta:
        model = models.category_sub_sub
        fields = '__all__'
        
class product_form(forms.ModelForm):
    class Meta:
        model = models.product
        fields = '__all__'