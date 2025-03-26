from django import forms
from back.models import Gallery,Image
from django.forms import modelformset_factory

class EditGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = ['owner']
        fields = '__all__'
        widgets={
            'galleryName':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gallery Name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class EditGalleryImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner']
        fields =['image']
        widgets ={
            'image':forms.ClearableFileInput(attrs={'class':'form-control'})
        }
EditGalleryImageFormset = modelformset_factory(Image,EditGalleryImageForm,extra=0)

