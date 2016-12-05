from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ILoveSuccess'
# using try/except block to handle error if counter is 0
def page_visit_counter():
    try:
        session['visit_counter'] += 1
    except KeyError:
        session['visit_counter'] = 1
# double() adds 1 but then reloads to add the second one
@app.route('/double', methods=['POST'])
def double():
    session['visit_counter'] += 1
    return redirect(url_for('index'))
# hack() resets it to 0 1 but then reloads to set the count at one
@app.route('/hack', methods=['POST'])
def hackcounter():
    session['visit_counter'] = 0
    return redirect(url_for('index'))
@app.route('/')
def index():
    page_visit_counter()
    return render_template ("index.html")
app.run(debug=True)
