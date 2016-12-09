from flask import Flask, flash, render_template, request, redirect, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# name_regex = re.compile(r'^[a-zA-Z]')
app = Flask(__name__)
app.secret_key = 'Before I die... I want to give away a million dollars.'
@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/results', methods=['POST'])
def result():
    errorFlag = "False"

    if str.isalpha(str(request.form['fname'])):
        print "First name OK"
    else:
        print "First name bad"
        flash("Please enter a valid first name.")
        errorFlag = "True"
    if str.isalpha(str(request.form['lname'])):
        print "Last name OK"
    else:
        print "Last name bad"
        flash("Please enter a valid last name.")
        errorFlag = "True"

    if len(request.form['email']) < 1:
        flash("Please enter your email address.")
        errorFlag = "True"
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address.")
    else:
        session['email'] = request.form['email']

    if len(request.form['password']) < 1:
        flash("Please enter a password.")
        errorFlag = "True"
    elif len(request.form['password']) < 9:
        flash("Please enter a password of at least 9 characters.")
    else:
        # flash("Success. Your name is {}".format(request.form['name']))
        session['password'] = request.form['password']

    if len(request.form['cpassword']) < 1:
        flash("Please enter your password twice to confirm your password.")
        errorFlag = "True"
    elif request.form['password'] != request.form['cpassword']:
        errorFlag = "True"
        flash("Your passwords don't match. Please enter the same password in the password and confirm password blocks.")

    if errorFlag == "True":
        return redirect ('/')
    else:
        return redirect ('/results')
@app.route('/results')
def show_result():
    return render_template('results.html')

app.run(debug=True)
