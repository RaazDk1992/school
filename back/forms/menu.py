from django import forms
from back.models import Menu, SubMenu, ContentType
from django.forms import modelformset_factory

class MenuForm(forms.ModelForm):
    contentType = forms.ModelChoiceField(
        queryset=ContentType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select a Content Type"
    )

    # Ensure viewRef is optional and has a default
    viewRef = forms.CharField(
        required=False, 
        initial="front.views.dynamicView",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'View Reference (Optional)'})
    )

    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'menuItem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu item name'}),
            'menuPath': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter menu path'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_expandable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.viewRef:  # Apply default if empty
            instance.viewRef = "front.views.dynamicView"
        if commit:
            instance.save()
        return instance


class SubMenuForm(forms.ModelForm):
    class Meta:
        model = SubMenu
        fields = ['submenu']
        widgets = {
            'submenu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Submenu Name'})
        }


SubMenuFormSet = modelformset_factory(SubMenu, form=SubMenuForm, extra=1)
