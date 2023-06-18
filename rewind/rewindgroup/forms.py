from django import forms
from .models import Buyer


class BuyBilet(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'email', 'count_bilet']
