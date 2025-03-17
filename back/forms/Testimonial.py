from django import forms 
from back.models import Testimonials

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields ='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name ','id':'date_picker'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message here..','id':'date_en'}),
            'image':forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'File'}),
            'extra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Extra info','id':'date_picker'}),
        }