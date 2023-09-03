from django.urls import path
from receipts.views import receipts_list, create_receipt, redirect


def redirect_to_receipts(request):
    return redirect("receipts")


urlpatterns = [
    path("", receipts_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
