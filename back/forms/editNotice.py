from django import forms
from django.forms import modelformset_factory
from django_ckeditor_5.widgets import CKEditor5Widget

from back.models import Notices, NoticeDocuments, NoticeImages

class NoticeFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].required = False

    class Meta:
        model = Notices
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter notice title'}),
            'body': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"),
        }

class NoticeImageFormEdit(forms.ModelForm):
    class Meta:
        model = NoticeImages
        exclude = ['owner']
        fields = ['id', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': False})
        }

class NoticeDocumentFormEdit(forms.ModelForm):
    class Meta:
        model = NoticeDocuments
        exclude = ['owner']
        fields = ['id', 'document']
        widgets = {
            'document': forms.FileInput(attrs={'class': 'form-control', 'required': False})
        }
