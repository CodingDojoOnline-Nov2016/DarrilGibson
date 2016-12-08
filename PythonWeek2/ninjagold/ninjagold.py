from flask import Flask, render_template, request, redirect, session, url_for
import time
from random import randint
app = Flask(__name__)
app.secret_key = 'ILoveSuccess'
@app.route('/')
def index():
    session['gold_score'] = 0
    log = ""
    # session['history']=[] # list of lists
    session['history']=[]
    # Didn't need to, but for fun, wrote activity log into a text file
    # just to experiment with how to do so
    # reset activity log
    open("Activities.txt","w").close()
    return render_template ("index.html")
@app.route('/process_money', methods=['POST'])
def process():
    place = request.form['building']
    timestamp = time.strftime("(%Y/%m/%d %I:%M %p)")
    if place == 'farm':
        random = randint(10,20)
        session['gold_score'] = session['gold_score'] + random
        print 'farm ' + str(random) + " " + timestamp
        log = "Earned " + str(random) + " golds from the farm " + timestamp
    elif place == 'cave':
        random = randint(5,10)
        session['gold_score'] = session['gold_score'] + random
        print 'cave ' + str(random) + " " + timestamp
        log = "Earned " + str(random) + " golds from the cave " + timestamp
    elif place == 'house':
        random = randint(2,5)
        session['gold_score'] = session['gold_score'] + random
        print 'house ' + str(random) + " " + timestamp
        log = "Earned " + str(random) + " golds from the house " + timestamp
    elif place == 'casino':
        # 1 for win, 0 for lose
        random = randint(0,50)
        winlose = randint(1,2)
        print 'winlose = ' +  str(winlose)
        if winlose == 1: #win
            session['gold_score'] = session['gold_score'] + random
            log = "Entered a casino and won " + str(random) + " golds. Woo Hoo! " + timestamp
        else: # lose
            session['gold_score'] = session['gold_score'] - random
            log = "Entered a casino and lost " + str(random) + " golds... Ouch. " + timestamp
        print 'casino ' + str(random) + " " + timestamp
    else:
        print 'no match'
    text_file = open("Activities.txt","a")
    text_file.writelines(log+"\n")
    text_file.close()
    session['history'].append(log)
    # Populate text area
    # dictObj = [{ a: session['log'], 'color': red }]
    # session['history'] = session['history'] + "\n" + session['log']
    # session['history'].append(dictObj)
    # print session['history']
    # session['activities'] = session['activities'] + "\n" + 'log'
    # read from file and populate textarea
    # with open("Activities.txt", "r") as log:
        # log = []
        # for line in log:
        #       log.append(line)
    #   log = activities.readlines()
    # print log
    return render_template ("index.html")

app.run(debug=True)
