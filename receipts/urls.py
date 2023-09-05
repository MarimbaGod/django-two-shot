from django.urls import path
from receipts.views import (
    receipts_list,
    create_receipt,
    redirect,
    expense_category_list,
    accounts_list,
    create_expense_category,
    create_account,
)


def redirect_to_receipts(request):
    return redirect("receipts")


urlpatterns = [
    path("", receipts_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", expense_category_list, name="category_list"),
    path("accounts/", accounts_list, name="accounts_list"),
    path(
        "categories/create/", create_expense_category, name="create_category"
    ),
    path("accounts/create/", create_account, name="create_account"),
]
