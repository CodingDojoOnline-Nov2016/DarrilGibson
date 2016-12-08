from flask import Flask, flash, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ILoveSuccess'
@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/results', methods=['POST'])
def result():
    print "Got Post Info"
    # Use errorFlag to determine which page to show
    errorFlag = "False"
    if len(request.form['name']) < 1:
        flash("Please enter your name.")
        errorFlag = "True"
    else:
        # flash("Success. Your name is {}".format(request.form['name']))
        session['name'] = request.form['name']
    if len(request.form['comments']) < 1:
        flash("Please enter a comment.")
        errorFlag = "True"
    if len(request.form['comments']) > 120:
        flash("Please limit your comments to 120 characters or less. You've entered {}".format(len(request.form['comments'])))
        # Put comments into session variable to populate text area with what the user already entered.
        session['comments'] = request.form['comments']
        errorFlag = "True"
    else:
        session['comments'] = request.form['comments']
    if errorFlag == "True":
        # flash("<img src='{{ url_for('static', filename='images/confused.png') }} alt=Confused >")
        return redirect ('/')
    else:
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        return redirect ('/results')
@app.route('/results')
def show_result():
    return render_template('results.html')
app.run(debug=True)
