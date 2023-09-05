from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import (
    CreateReceiptForm,
    CreateExpenseForm,
    CreateAccountForm,
)


# Create your views here.
@login_required
def receipts_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = CreateReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


@login_required
def create_expense_category(request):
    if request.method == "POST":
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            return redirect(
                "category_list"
            )  # named in receipts.urls category path
    else:
        form = CreateExpenseForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_expense_form.html", context)


@login_required
def expense_category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    for category in categories:
        category.receipts_count = Receipt.objects.filter(
            category=category
        ).count()

        context = {
            "categories": categories,
        }
        return render(request, "receipts/categories.html", context)


@login_required
def accounts_list(request):
    accounts = Account.objects.filter(owner=request.user)
    for account in accounts:
        account.receipts_count = Receipt.objects.filter(
            account=account
        ).count()

        context = {
            "accounts": accounts,
        }
        return render(request, "receipts/accounts_list.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect("accounts_list")
    else:
        form = CreateAccountForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_account.html", context)
