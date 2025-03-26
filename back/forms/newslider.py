from django import forms 
from django.forms import formset_factory
from back.models import Sliders
class SliderForm(forms.ModelForm):
    class Meta:
        model = Sliders
        fields ='__all__'
        exclude = ['owner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter  brief desc name'}),
            'image': forms.ClearableFileInput(attrs={'id': 'file'}) 
        }
    
SliderFormSet = formset_factory(SliderForm,extra=1)