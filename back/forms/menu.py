# forms.py
from django import forms
from back.models import Menu, SubMenu,ContentType
from django.forms import modelformset_factory

class MenuForm(forms.ModelForm):
    contentType = forms.ModelChoiceField(
        queryset=ContentType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select a Content Type"
    )
    class Meta:
        model = Menu
        fields = '__all__'
       
        widgets = {
            'menuItem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item name'}),
            'menuPath': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu path'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_expandable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

class SubMenuForm(forms.ModelForm):
    class Meta:
        model = SubMenu
        fields = ['submenu']
        widgets = {
            'submenu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Submenu Name'})
        }

SubMenuFormSet = modelformset_factory(SubMenu, form=SubMenuForm, extra=1)
