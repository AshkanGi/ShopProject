from django import forms
from .models import Address


class AddAddressForm(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = Address
        fields = '__all__'
