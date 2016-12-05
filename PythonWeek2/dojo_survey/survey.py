from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    return render_template ("index.html")
@app.route('/results', methods=['POST'])
def result():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect ('/results')
@app.route('/results')
def show_result():
    return render_template('results.html')
app.run(debug=True)
