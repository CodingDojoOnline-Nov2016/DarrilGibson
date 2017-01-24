from django.shortcuts import render, redirect, HttpResponse
from . models import User

def index(request):
    return render(request, "email_chk/index.html")

def check_email(request):
    print request
    if request.method == "POST":
        email_check = User.objects.register(request.POST['email'])
        print email_check
        if email_check[0]: # if exists, Email is valid
            # clear errors
            request.session['errors'] = []
            request.session['msg'] = "The email address you entered is a valid email address. Thank you."
            # Go to to Success page to show users
            return redirect('/success')
        else: #Email is not valid
            print email_check[1]
            request.session['errors'] = email_check[1]
            return redirect('/')

def success(request):
    users = User.objects.all()
    print users
    context = {
        "users": users
    }
    return render(request, "email_chk/success.html", context)

def destroy(request, id):
    action = User.objects.deleteuser(id)
    request.session['msg'] = "Email address deleted."
    return redirect('/success')
