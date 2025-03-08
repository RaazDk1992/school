from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from back.models import Notices

class NoticeForm(forms.ModelForm):
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
            'document': forms.ClearableFileInput(attrs={'id': 'file'}) 
        }
