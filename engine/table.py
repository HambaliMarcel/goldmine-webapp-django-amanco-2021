from django import forms
from engine.models import Source


class EngineForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['source', 'auth', 'role']
        widgets = {
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'auth': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
        }
