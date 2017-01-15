from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print "in index"
    return render(request, 'surveyform/index.html ')

def process(request):
    print "in process"
    return render(request, 'surveyform/index.html')

def process(request):
    print "Got Post Info"
    print request.POST
    request.session['count'] = request.session['count'] + 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/results')

def results(request):
    return render(request, 'surveyform/results.html')
