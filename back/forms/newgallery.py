from django import forms
from back.models import Gallery,Image
from django.forms import modelformset_factory

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        widgets={
            'galleryName':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gallery Name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =['image']
        widgets ={
            'image':forms.ClearableFileInput(attrs={'class':'form-control','hidden':True})
        }
GalleryImageFormset = modelformset_factory(Image,GalleryImageForm,extra=1)

