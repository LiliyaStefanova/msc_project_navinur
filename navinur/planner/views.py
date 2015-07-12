from django.shortcuts import render

# Create your views here.

def plan_trip(request):
    tms_url = "http://" + request.get_host() + "/tms/"

    return render(request, "select_points.html",
                  {'tms_url': tms_url})
