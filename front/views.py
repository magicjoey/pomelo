from django.shortcuts import render
from django.utils.translation import ugettext
# Create your views here.
from front.models import Nav


def index(request):

    return render(request, "front/index.html", {"nav_list": __nav()})

def detail(request):

    return render(request, "front/detail.html", {"nav_list": __nav()})

def index_bak(request):
    return render(request, "front/bak/index_bak.html")


def service(request):
    return render(request, "front/service.html", {"nav_list": __nav()})

def app(request):
    return render(request, "front/app.html", {"nav_list": __nav()})

def contact(request):
    return render(request, "front/contact.html", {"nav_list": __nav()})

def about(request):
    return render(request, "front/about.html", {"nav_list": __nav()})

def child(request):
    return render(request, "front/child.html", {"nav_list": __nav()})

def element(request):
    return render(request, "front/element.html", {"nav_list": __nav()})


def portfolio(request):
    return render(request, "front/portfolio.html", {"nav_list": __nav()})


def __nav():
    nav_list = Nav.objects.filter(level__in=[1, None]).order_by("priority")
    return nav_list