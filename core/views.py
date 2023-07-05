from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request, "core/about.html", {})


def index(request):
    return render(request, "core/index.html", {})


def store(request):
    return render(request, "core/store.html", {})
