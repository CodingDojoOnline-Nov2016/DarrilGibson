from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    print "in index"

    cur_date = datetime.now().strftime ("%B %d, %Y")
    cur_time = datetime.now().strftime ("%I:%M %p")
    print cur_date
    print cur_time
    context = {
    "cur_date":cur_date, "cur_time":cur_time
    }
    # now = datetime()
    return render(request,'timedisplay/index.html', context)
