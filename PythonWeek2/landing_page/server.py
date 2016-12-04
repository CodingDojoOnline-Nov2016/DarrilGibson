from flask import Flask, render_template
from random import randint
app = Flask(__name__)
@app.route('/')
def index():
    return render_template ("index.html", phrase="Hello Bart",python_zen=python_zen)
        # return render_template ("index.html", phrase="Hello Bart", times=5)
@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/dojos/basic')
def dojosbasic():
    return render_template('dojos/dojosbasic.html')

@app.route('/dojos/new/dojos')
def dojos():
    return render_template('/dojos/new/dojos.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')
python_zens = ["Beautiful is better than ugly.",
                "Explicit is better than implicit.",
                "Simple is better than complex.",
                "Complex is better than complicated.",
                "Flat is better than nested.",
                "Sparse is better than dense.",
                "Readability counts.",
                "Special cases aren't special enough to break the rules.",
                "Although practicality beats purity.",
                "Errors should never pass silently.",
                "Unless explicitly silenced.",
                "In the face of ambiguity, refuse the temptation to guess.",
                "There should be one-- and preferably only one --obvious way to do it.",
                "Although that way may not be obvious at first unless you're Dutch.",
                "Now is better than never.",
                "Although never is often better than *right* now.",
                "If the implementation is hard to explain, it's a bad idea.",
                "If the implementation is easy to explain, it may be a good idea.",
                "Namespaces are one honking great idea -- let's do more of those.",]

random_number = randint(0,len(python_zens)-1)
python_zen = python_zens[random_number]
app.run(debug=True)
