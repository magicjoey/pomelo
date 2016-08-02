from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "front/index.html")

def index_bak(request):
    return render(request, "front/index_bak.html")


def service(request):
    return render(request, "front/service.html")


def contact(request):
    return render(request, "front/contact.html")


def element(request):
    return render(request, "front/element.html")


def portfolio(request):
    return render(request, "front/portfolio.html")