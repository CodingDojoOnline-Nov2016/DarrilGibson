from flask import Flask, render_template, request, redirect, session, url_for
import random
from random import randint
app = Flask(__name__)
app.secret_key = 'ILoveSuccess'
@app.route('/')
def index():
    session['random'] = (random.randrange(0, 101))
    # session['random'] = randint(0,101)
    print session['random']
    session['guess_feedback'] = ""
    session['guess'] = 0
    print session['guess']
    print type(session['random'])
    print type(session['guess'])
    session['intCounter'] = 0
    return render_template ("index.html")
@app.route('/guess', methods=['POST'])
def guess():
    session['intCounter'] = session['intCounter'] + 1
    session['guess'] = int(request.form['number'])
    print session['random']
    print session['guess']
    print type(session['guess'])
    print type(session['random'])
    #Didn't work until I converted numbers to strings
    if int(session['guess']) == session['random']:
        print 'match'
    elif int(session['guess']) < session['random']:
        print 'too low'
    elif int(session['guess']) > session['random']:
        print 'too high'
    else:
        print 'no match'
    return render_template ("index.html")
app.run(debug=True)
