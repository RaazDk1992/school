# forms.py
from django import forms
from back.models import Menu, SubMenu
from django.forms import modelformset_factory

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menuItem', 'is_active', 'is_expandable']
        widgets = {
            'menuItem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_expandable': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class SubMenuForm(forms.ModelForm):
    class Meta:
        model = SubMenu
        fields = ['submenu']
        widgets = {
            'submenu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Submenu Name'})
        }

SubMenuFormSet = modelformset_factory(SubMenu, form=SubMenuForm, extra=1)
