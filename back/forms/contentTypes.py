from django import forms
from back.models import ContentType

class ContentTypeForm(forms.ModelForm):
    class Meta:
        model = ContentType
        exclude = ['owner']
        fields = '__all__'
        widgets ={
            'contentType':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item name'})
        }