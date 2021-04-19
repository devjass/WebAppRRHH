from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['nombre1', 'nombre2', 'apellido1','apellido2','pais', 'tipoId','numeroId','fechaIngreso','order']
        widgets = {
            'nombre1': forms.TextInput(attrs={'class':'form-control'}),
            'nombre2': forms.TextInput(attrs={'class':'form-control'}),
            'apellido1': forms.TextInput(attrs={'class':'form-control'}),
            'apellido2': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'tipoId': forms.TextInput(attrs={'class':'form-control'}),
            'numeroId': forms.TextInput(attrs={'class':'form-control'}),
            'fechaIngreso': forms.DateTimeInput(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
