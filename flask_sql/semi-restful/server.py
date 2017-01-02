from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# re for regex
import re
app = Flask(__name__)
app.secret_key = "Rest, rested, resting, restful"
mysql = MySQLConnector(app, 'users')
# Regex for email
regex_email=r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$'
# Simple regex pattern for names
regex_name=r'^[a-zA-Z\',.-]+$'

#  (defaults to GET)
@app.route('/')
def index():
    select_query = ('SELECT id, first_name, last_name, email, created_at FROM users')
    users = mysql.query_db(select_query)
    return render_template('index.html',users=users)

#  a GET request to /users - calls the index method to display all the users.
# This will need a template.
#  (defaults to GET)
@app.route('/users')
def users():
    return redirect('/')
    # return render_template('index.html')

# GET request to /users/new - calls the new method to display a form
# allowing users to create a new user. This will need a template.
@app.route('/users/new')
def new():
    return render_template('new.html')

# GET request /users/<id>/edit - calls the edit method to display a form
# allowing users to edit an existing user with the given id.
# This will need a template.
@app.route('/users/<id>/edit')
def edit(id):
    data = {'id': id}
    select_query = ('SELECT id, first_name, last_name, email FROM users WHERE id=:id')
    user = mysql.query_db(select_query, data)
    return render_template('edit.html', user=user, id=id)

# GET /users/<id> - calls the show method to display the info for a
# particular user with given id. This will need a template.
@app.route('/users/<id>')
def show(id):
    data = {'id': id}
    select_query = ('SELECT id, first_name, last_name, email, created_at FROM users WHERE id=:id')
    user = mysql.query_db(select_query, data)
    return render_template('show.html', user=user)

# POST to /users/create - calls the create method to insert a new user record
# into our database. This POST should be sent from the form on the
# page /users/new. Have this redirect to /users/<id> once created.
@app.route('/users/create', methods=['POST'])
def create():
    errors=[]
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    # Validation for each field
    if len(first_name) < 2:
        errors.append('Please enter a first name')
    elif not re.match(regex_name,first_name):
        errors.append('Please enter a valid first name (no numbers or special characters)')

    if len(last_name) < 2:
        errors.append('Please enter a last name')
    elif not re.match(regex_name,last_name):
        errors.append('Please enter a valid last name (no numbers or special characters)')

    if not re.match(regex_email,email):
        errors.append('Please enter a valid email address')

    if errors:
        for error in errors:
            flash(error)
        return render_template('new.html', first_name=first_name, last_name=last_name, email=email)
    else:
        # no errors - build and run query
        data = {
                 'first_name': first_name,
                 'last_name':  last_name,
                 'email': email
               }
        insert_query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) \
                  VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        mysql.query_db(insert_query, data)
    return redirect('/')    #users/create

@app.route('/users/<id>/destroy')
def destroy(id):
    data = {'id': id}
    delete_query = ('DELETE FROM users WHERE id =:id')
    result_comments = mysql.query_db(delete_query, data)
    return redirect('/')

# POST /users/<id> - calls the update method to process the submitted form
# sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
@app.route('/users/<id>', methods=['POST'])
def update(id):
    data = {'id': id}
    # Compare to create method
    errors=[]
    first_name = request.form['first_name']
    print first_name
    last_name = request.form['last_name']
    print last_name
    email = request.form['email']
    print email
    print "before validation"
    # Validation for each field
    if len(first_name) < 2:
        errors.append('Please enter a first name')
    elif not re.match(regex_name,first_name):
        errors.append('Please enter a valid first name (no numbers or special characters)')

    if len(last_name) < 2:
        errors.append('Please enter a last name')
    elif not re.match(regex_name,last_name):
        errors.append('Please enter a valid last name (no numbers or special characters)')

    if not re.match(regex_email,email):
        errors.append('Please enter a valid email address')

    if errors:
        for error in errors:
            flash(error)
        return render_template('edit.html', first_name=first_name, last_name=last_name, email=email, id=id)
    else:
        # no errors - build and run query
        update_query = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id"
        data = {
                 'id': id,
                 'first_name': first_name,
                 'last_name':  last_name,
                 'email': email
               }
        mysql.query_db(update_query, data)

    return redirect('/')

# Filter function to add letters to day. Receives "date" and passes back "day" as number with letters
# 'st for 1, 21, 31' # 'nd for 2, 22' # 'rd for 3, 23'
# 'th for 4, 5, 6, 7, 8, 9, 10, 11, 24, 25,26,27,28,29,30'
@app.template_filter('day')
def _jinja2_filter_day(date):
    day = date.strftime('%d')
    if day == 1:
        letters = "st"
    elif day == 2:
        letters = "nd"
    elif day == 3:
        letters = "rd"
    elif day == 21:
        letters = "st"
    elif day == 22:
        letters = "nd"
    elif day == 23:
        letters = "rd"
    elif day == 31:
        letters = "st"
    else:
        letters = "th"
    # Remove zero padding for days 1-9 (i.e. instead of 01, it will be 1)
    if int(day) < 10:
        day = day.lstrip('0')
    day = day+letters
    return day

app.run(debug=True)
