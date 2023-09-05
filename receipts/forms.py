from django import forms
from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory, Account


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


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
        ]


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "name",
            "number",
        ]
