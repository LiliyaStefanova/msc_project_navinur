from django.shortcuts import render

# Create your views here.

def display_map(request):
    tms_url = "http://" + request.get_host() + "/tms/"

    return render(request, "main.html",
                  {'tms_url': tms_url})

