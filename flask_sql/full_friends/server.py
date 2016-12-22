from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "When there isn't a tutorial, what words do you need to say to get help?"
mysql = MySQLConnector(app, 'friendsdb')
# Regex for email
regex_email=r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$'
# Simple regex pattern for names
# regex_name=r'^[a-zA-Z]'
regex_name=r'^[a-zA-Z\',.-]+$'

# Show all users in database (defaults to GET) 
@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    print users
    return render_template('index.html', all_users=users)

# Delete a user from database
@app.route('/friends/<id>/destroy', methods=['POST'])
def destroy(id):
    data = {'id': id}
    user = mysql.query_db('DELETE FROM users WHERE id=:id', data)
    return redirect('/')

# Display a record on new page to edit (defaults to GET)
@app.route('/friends/<id>/edit')
def edit(id):
    data = {'id': id}
    user = mysql.query_db('SELECT * FROM users WHERE id=:id', data)
    return render_template('edit.html', user=user[0])

# Update record from edit.html
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

# Create a user record
@app.route('/friends', methods=['POST'])
def create():
    errors=[]
    print request.form['first_name']
    print request.form['last_name']
    print request.form['email']
    # Need validation for each field
    if len(request.form['first_name']) < 2:
        errors.append('Please enter a first name')
    elif not re.match(regex_name,request.form['first_name']):
        errors.append('Please enter a valid first name (no numbers or special characters)')

    if len(request.form['last_name']) < 2:
        errors.append('Please enter a last name')
    elif not re.match(regex_name,request.form['last_name']):
        errors.append('Please enter a valid last name (no numbers or special characters)')

    email = request.form['email']
    if not re.match(regex_email,email):
        errors.append('Please enter a valid email address')

    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        # no errors - build and run query
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) \
                  VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email']
               }
        mysql.query_db(query, data)
    return redirect('/')

@app.route("/notes")
def notes():
    return render_template("notes.html")

# @app.route('/show_friend/<friend_id>', methods=['POST'])
@app.route('/show_friend', methods=['POST'])
# def show(friend_id):
def show():
    friend_id = request.form['id']
    print friend_id
    # print friend_id
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM users WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    print "show"
    print friends
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('show_friend.html')
    # return render_template('index.html', one_friend=friends[0])


# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
    # print request.form['id']
    # print "Friend_ID" + friend_id
    # query = "UPDATE friends \
    #          SET first_name = :first_name, last_name = :last_name, occupation = :occupation \
    #          WHERE id = :id"
    # data = {
    #          'first_name': request.form['first_name'],
    #          'last_name':  request.form['last_name'],
    #          'occupation': request.form['occupation'],
    #          'id': friend_id
    #        }
    # mysql.query_db(query, data)
    # return redirect('/', friend_id=friend_id)

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
