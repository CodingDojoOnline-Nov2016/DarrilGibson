from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    return render(request, "loginregistration/index.html")

def login(request):
    print "in login"
    email = request.POST['email']
    request.session['email'] = email
    action = User.objects.login(email, request.POST['password'])

    if action == True: # login successful
        request.session['msg'] = "You are now logged on."
        return render(request, 'loginregistration/success.html')
    else: #errors
        request.session['msg'] = "Incorrect email address or password."
        return render(request, 'loginregistration/index.html')
    return redirect('/')

def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        request.session['firstname'] = first_name
        last_name = request.POST['lastname']
        request.session['lastname'] = last_name
        email = request.POST['email']
        request.session['email'] = email
        # action = User.objects.register(request)
        errors = User.objects.register(first_name, last_name, request.POST['password'], request.POST['confirm_pw'], email)
        request.session['errors'] = errors
        context = {
            "errors": errors
        }
        if errors[0] == True: # No errors
            print "no errors True"
            request.session['msg'] = "You have successfully registered."
            return render(request, 'loginregistration/success.html')
        else: #errors
            return render(request, 'loginregistration/index.html', context)

def success(request):
    return redirect('/')

def destroy(request, id):
    action = User.objects.deleteuser(id)
    request.session['msg'] = "Email address deleted."
    return redirect('/show')

def show(request):  #used for debugging (Wanted to see what's being created)
    users = User.objects.all()
    print users
    context = {
        "users": users
    }
    return render(request, "loginregistration/show.html", context)
