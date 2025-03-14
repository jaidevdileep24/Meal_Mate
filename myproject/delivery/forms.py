from django import forms
from .models import Restaurants,Menu

class ResForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['res_name','food_cat','food_cat','img','res_address']
        
class AddMenu(forms.ModelForm):
    class Meta:
        model= Menu
        fields = ['res','item_name', 'desc', 'price', 'is_avial', 'category']
        

        