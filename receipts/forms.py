from django import forms
from django.forms import ModelForm
from receipts.models import Receipt


class CreateReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]
