from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def index(request):
    now=datetime.datetime.now()
    return render(request, "newmonth/index.html", {
        "newmonth": now.day == 1
    })

