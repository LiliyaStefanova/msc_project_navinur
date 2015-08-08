from django.shortcuts import render
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navinur.settings")
# Create your views here.


def display_map(request):
    tms_url = "http://" + request.get_host() + "/tms/"

    return render(request, "main.html",
                  {'tms_url': tms_url})

