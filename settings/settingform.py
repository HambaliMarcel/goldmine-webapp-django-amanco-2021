from django import forms
from .models import setting


class settingform(forms.ModelForm):
    class Meta:
        model = setting
        fields = [
            'param_def',
            'schedule',
            'exptype',
            'export',
            'uname',
        ]
