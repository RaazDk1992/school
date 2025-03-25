from django import forms 
from back.models import Dynamic
from django_ckeditor_5.widgets import CKEditor5Widget


class DynamicForm(forms.ModelForm):
    class Meta:
        model = Dynamic
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Content Title'}),
            'body':CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"),
            'image': forms.ClearableFileInput(attrs={'id': 'file'}) ,
            'files':forms.ClearableFileInput(attrs={'id': 'file'}) ,
            
        }