from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.base_user import BaseUserManager

# Create your views here.
# Using make_random_password to create 14 character string
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    if 'rnd_word' not in request.session:
        rnd_word = BaseUserManager().make_random_password(length=14, allowed_chars='abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        request.session['rnd_word'] = rnd_word
        print rnd_word
    return render(request, 'random_word/index.html')

def generate(request):
    print (request.method)
    if request.method == "POST":
        print ('*'*20)
        print request.POST
        print ('*'*20)
        rnd_word = BaseUserManager().make_random_password(length=14, allowed_chars='abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        request.session['rnd_word'] = rnd_word
        request.session['count'] = request.session['count'] + 1
        return redirect('/')
