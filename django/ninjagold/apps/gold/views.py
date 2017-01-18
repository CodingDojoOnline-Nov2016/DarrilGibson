from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from random import randint

# Create your views here.
def index(request):
    print "in index"
    print request
    request.session['gold_score'] = 0
    request.session['history'] = []
    return render(request, "gold/index.html")

def process_money(request):
    print request
    place = request.POST['building']
    # place = request.form['building']
    timestamp = datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
    if place == 'farm':
        random = randint(10,20)
        request.session['gold_score'] = request.session['gold_score'] + random
        print 'farm ' + str(random) + " " + timestamp
        log = "Earned " + str(random) + " golds from the farm " + timestamp
    elif place == 'cave':
        random = randint(5,10)
        request.session['gold_score'] = request.session['gold_score'] + random
        print 'cave ' + str(random) + " " + timestamp
        log = "Earned " + str(random) + " golds from the cave " + timestamp
    elif place == 'house':
        random = randint(2,5)
        request.session['gold_score'] = request.session['gold_score'] + random
        print 'house ' + str(random) + " " + timestamp
        log = "Earned " + str(random) + " golds from the house " + timestamp
    elif place == 'casino':
        # 1 for win, 0 for lose
        random = randint(0,50)
        winlose = randint(1,2)
        print 'winlose = ' +  str(winlose)
        if winlose == 1: #win
            request.session['gold_score'] = request.session['gold_score'] + random
            log = "Entered a casino and won " + str(random) + " golds. Woo Hoo! " + timestamp
        else: # lose
            request.session['gold_score'] = request.session['gold_score'] - random
            log = "Entered a casino and lost " + str(random) + " golds... Ouch. " + timestamp
            log = ('<p style="color:red">' + log + '</p>')
        print 'casino ' + str(random) + " " + timestamp
    else:
        print 'no match'
    request.session['history'].append(log)
    return render(request, "gold/index.html")
