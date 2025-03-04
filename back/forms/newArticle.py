from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from back.models import Article

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item name'}),
            'body':CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"),
            'image': forms.ClearableFileInput(attrs={'id': 'file'}) 
        }
