from django.forms import ModelForm
from .models import *
from django import forms
from .models import CreditSale
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to']


class CreditSaleForm(forms.ModelForm):
    class Meta:
        model = CreditSale
        fields = ['product', 'client_name', 'quantity', 'id_nin_number', 'contact', 'address', 'branch']