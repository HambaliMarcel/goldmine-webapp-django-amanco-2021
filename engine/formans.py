from django import forms


class Formans(forms.Form):
    source = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Source Website'
    }))
    auth = forms.BooleanField(widget=forms.CheckboxInput)
    role = forms.ChoiceField(widget=forms.Select)
