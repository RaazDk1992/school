from django import forms
from back.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields ='__all__'
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter quote here', 'rows':2,'cols':10}),
            'image': forms.ClearableFileInput(attrs={'id': 'file'}) 
        }