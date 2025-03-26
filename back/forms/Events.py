from django import forms 
from back.models import Events

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields='__all__'
        exclude = ['owner'] 
        widgets = {
            'date_np': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose date','id':'date_picker'}),
            'date_en': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Choose date','id':'date_en'}),
            'event':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter  Event name'}),
        }
    

