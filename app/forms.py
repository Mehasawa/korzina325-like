from django import forms
from django.core.validators import RegexValidator


class Myforms(forms.Form):
    adres = forms.CharField()
    name = forms.CharField()
    tel = forms.CharField(validators=[RegexValidator('[+7][0-9]{10}',
                            message= 'neok')])