from django import forms
from back.models import Menu
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        widgets ={
                'menuItem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item name'}),
                'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
                'is_expandable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


        }