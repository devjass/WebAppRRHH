from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['nombre1', 'nombre2','order']
        widgets = {
            'nombre1': forms.TextInput(attrs={'class':'form-control'}),
            'nombre2': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
