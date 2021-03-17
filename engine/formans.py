from django import forms
from .models import Source


class Formans(forms.ModelForm):
    class Meta:
        model = Source
        fields = [
            'source',
            'auth',
            'role',
        ]
