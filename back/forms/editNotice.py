from django import forms
from django.forms import modelformset_factory
from django_ckeditor_5.widgets import CKEditor5Widget

from back.models import Notices,NoticeDocuments,NoticeImages

class NoticeFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["noticeBody"].required = False


    class Meta:
        model = Notices
        fields = '__all__'
        widgets = {
            'noticeTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter notice title'}),
            'noticeBody':CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"),
           
        }
class NoticeImageFormEdit(forms.ModelForm):
    class Meta:
        model = NoticeImages
        fields =['id','image']
        widgets ={
            'image':forms.ClearableFileInput(attrs={'class':'form-control','required':False})
        }

class NoticeDocumentFormEdit(forms.ModelForm):
    class Meta:
        model = NoticeDocuments
        fields =['id','document']
        widgets ={
            'document':forms.ClearableFileInput(attrs={'class':'form-control','required':False})
        }


