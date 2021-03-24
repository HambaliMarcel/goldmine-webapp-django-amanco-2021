from django import forms
from settings.models import parameter


class paramform(forms.ModelForm):
    class Meta:
        model = parameter
        fields = ['param', 'desc']
        widgets = {
            'param': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
