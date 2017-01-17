from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings

# Create your views here.
# Goal - keep these 'views less 20 lines (minimal)
# instead, they should be in models (models.py)
def index(request):
    print "in index"
    print request
    request.session.color = ""
    return render(request, "ninjas/index.html")

def ninjas(request): # "display all ninjas"
    print "in ninjas"
    request.session.color = ""
    print request.session.color
    return render(request, "ninjas/ninjas.html")

def ninjacolor(request, color):
    print "in color"
    print request
    print color
    request.session.color = color
    return render(request, "ninjas/ninjas.html")
