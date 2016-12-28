from flask import Flask, request, redirect, render_template, session, flash
from random import randint
from mysqlconnection import MySQLConnector
# to handle sql exceptions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
# to encrypt password
from flask_bcrypt import Bcrypt
# for regex check of email and name
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Finally figured out these extend blocks"
mysql = MySQLConnector(app, 'thewall')
# Regex for email
regex_email=r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$'
# Simple regex pattern for names
regex_name=r'^[a-zA-Z\',.-]+$'

#  (defaults to GET)
@app.route('/')
def index():
    # put lyric in session so that I don't have to pass it every page
    session['lyric'] = lyric
    # use try except to test for existing session login
    try:
        # Send user to the Wall if logged in
        if session['login'] == "True":
            return redirect('/wall')
    except KeyError as e:
        # KeyError occurs if session['login'] doesn't exist
        # show index page if user not logged in
        return render_template('index.html')
    # return render_template('index.html')

#  (defaults to GET)
@app.route('/logoff')
def logoff():
    # session['login'] = "False"
    session.clear()
    return redirect ('/')
    # return render_template('index.html')

#  (defaults to GET)
@app.route('/showregister')
def showregister():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    errors=[]
    first_name = request.form['first_name']
    print first_name
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    #Check for valid first name
    if len(request.form['first_name']) < 2:
        errors.append('Please enter a first name')
    elif not re.match(regex_name,request.form['first_name']):
        errors.append('Please enter a valid first name (no numbers or special characters)')
    #Check for valid last name
    if len(request.form['last_name']) < 2:
        errors.append('Please enter a last name')
    elif not re.match(regex_name,request.form['last_name']):
        errors.append('Please enter a valid last name (no numbers or special characters)')
    #Check for valid email
    if not re.match(regex_email,email):
        errors.append('Please enter a valid email address as your username')
    #Check for valid password
    if len(request.form['password']) < 8:
        errors.append('Please enter a password at least 8 characters long')
    else:
        #Ensure passwords are the same
        if request.form['password'] != request.form['confirm_pw']:
            errors.append('Passwords do not match')
    if errors:
        for error in errors:
            flash(error)
            # include variables to display in form so user doesn't have to add them again
        return render_template('register.html', first_name=first_name, last_name=last_name, email=email)
    else:
        # Entered data is valid. Use Try Except to check for integrity error (from duplicate email)
        # Database email column has Unique flag set
        try:
            password = bcrypt.generate_password_hash(password)
            insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
                VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
            query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password }
            mysql.query_db(insert_query, query_data)
            session['login'] = "True"
            session['first_name'] = first_name
            # return render_template('wall.html')
            return redirect('/wall')
        except exc.IntegrityError as e:
            flash("This email address already exists in the database. Please use a different email address.")
            session['login'] = "False"
            return render_template('register.html')
        except Exception as e:
            flash("Unexpected error. Please try again.")
            session['login'] = "False"
            return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    errors=[]
    email = request.form['email']
    password = request.form['password']
    if not re.match(regex_email,email):
        errors.append('Please enter a valid email address as your username')
    if len(password)<8:
        errors.append('Please enter a valid password')
    if errors:
        for error in errors:
            flash(error)
        return render_template('index.html', email=email)
    else:
        data = {'email': email}
        user = mysql.query_db('SELECT id, first_name, email, password FROM users WHERE email=:email LIMIT 1', data)
        # check for existence of email address in database
        if user == []:
            # Don't tell potential hacker that email address is or isn't valid
            flash('Sorry, but your credentials aren\'t recognized.')
            print "email address not in database"
            return render_template('index.html', email=email)
        else:
            # valid email - check password
            if bcrypt.check_password_hash(user[0]['password'], password):
                session['login'] = "True"
                print session['login']
                # Store user id for posting messages and comments
                session['id'] = user[0]['id']
                session['first_name'] = user[0]['first_name']
                print session['id']
                return redirect('/wall')
            else:
                flash('Sorry, but your credentials aren\'t recognized.')
                return redirect('/')

@app.route('/wall')
def wall():
    # if not logged in, redirect to index page
    try:
        if session['login'] == "True":
            message_query = ('SELECT users.id, users.first_name, users.last_name, \
              messages.id as msgid, messages.message, messages.created_at \
              FROM messages join users ON users.id=messages.user_id \
              ORDER BY messages.created_at DESC')
            messages = mysql.query_db(message_query)

            comment_query = ('SELECT comments.comment, comments.user_id, comments.message_id, comments.created_at, \
                 messages.id, messages.user_id, users.first_name, users.last_name \
                 FROM comments JOIN users ON comments.user_id = users.id \
                 JOIN messages ON comments.message_id = messages.id \
                 ORDER BY comments.created_at DESC')
            comments = mysql.query_db(comment_query)
    except KeyError as e:
        # KeyError occurs if session['login'] doesn't exist
        # show index page if user not logged in
        return render_template('index.html')
    return render_template('wall.html',messages=messages, comments=comments)

@app.route('/postmessage', methods=['POST'])
def postmessage():
    errors=[]
    message = request.form['message']
    # Verify message has data
    if len(message) < 5:
        flash("Please enter a message.")
    else:
        # Write message to database
        user_id = session['id']
        query_data = { 'message': message, 'user_id': user_id }
        insert_query = "INSERT INTO messages (message, created_at, updated_at, user_id) \
            VALUES (:message, NOW(), NOW(), :user_id)"
        mysql.query_db(insert_query, query_data)
        print insert_query
        # return render_template('wall.html')
    return redirect('/wall')

@app.route('/addcomment', methods=['POST'])
def addcomment():
    errors=[]
    comment = request.form['comment']
    message_id = request.form['msgid']
    print comment
    # Verify comment has data
    if len(comment) < 5:
        print "error"
        flash("Please enter a message.")
        print "error"
    else:
        # Write comment to database
        user_id = session['id']
        query_data = { 'comment': comment, 'message_id': message_id, 'user_id': user_id }
        insert_query = ('INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) \
            VALUES (:comment, NOW(), NOW(), :user_id, :message_id) ')
        mysql.query_db(insert_query, query_data)
    return redirect('/wall')

@app.route('/deletemessage/<id>/delete', methods=['POST'])
def deletemessage(id):
    # Check to see if comments exist for message
    message_id = id
    query_data = {'message_id': message_id}
    select_query = ('SELECT * FROM comments WHERE message_id =:message_id')
    result_comments = mysql.query_db(select_query, query_data)
    if result_comments != []:
        # Comments exist for this message, delete them first
        # Use query_data from from select query a few lines up in this def
        delete_query = ('DELETE FROM comments WHERE message_id =:message_id')
        result_comments = mysql.query_db(delete_query, query_data)
    # Delete message
    delete_query = ('DELETE FROM messages WHERE id =:id')
    query_data = {'id': id}
    mysql.query_db(delete_query, query_data)
    return redirect('/wall')

pink_floyd = ["We don't need no education -The Wall",
    "We don't need no thought control -The Wall",
    "No dark sarcasm in the classroom -The Wall",
    "Teachers leave them kids alone -The Wall",
    "Hey! Teachers! Leave them kids alone! -The Wall",
    "All in all it's just another brick in the wall. -The Wall",
    "All in all you're just another brick in the wall. -The Wall"]
random_number = randint(0,len(pink_floyd)-1)
lyric = pink_floyd[random_number]

app.run(debug=True)
