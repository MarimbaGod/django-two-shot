from django.shortcuts import render
from receipts.models import Receipt


# Create your views here.
# unsure about how well I did at defining this view function...
def receipts_list(request):
    receipts = Receipt.objects.all
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


# im not sure why I named things reciepts, or why I use c
