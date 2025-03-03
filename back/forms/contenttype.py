from django import forms 
from back.models import ContentTypes
class ContentTypeForm(forms.ModelForm):
    class Meta:
        model = ContentTypes
        fields = "__all__"
        widgets ={
                    'contentType': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Content Type: Like: Notice / blog '}),
                    'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            }