from django.shortcuts import render
from services.models import Services


# Create your views here.
def services(request):
    serv = Services.objects.all()
    return render(request, "services/services.html", {'services': serv})
