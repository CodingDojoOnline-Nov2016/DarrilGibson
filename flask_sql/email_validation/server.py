from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "What Will Your Legacy Be"
# Added email_addresses table to mydb database
mysql = MySQLConnector(app, 'mydb')
# print mysql.query_db("SELECT * FROM email_addresses")
# Regex for email
regex_pattern=r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def email():
    session['name'] = request.form['email']
    print request.form['email']
    # Validate entered email address
    email = request.form['email']
    if not re.match(regex_pattern,email):
        print "Please enter a valid email address"
        # errorDiv.removeClass(hidden)
        flash("Please enter a valid email address")
    else:
        # write email address to database
        # Build query
        query = "INSERT INTO email_addresses (email_address, created_at, updated_at) \
             VALUES (:email_address, NOW(), NOW())"
        # Name data
        data = {
                 'email_address': request.form['email']
               }
        # Run query to insert address
        mysql.query_db(query, data)
        # show email addresses:
        emails = mysql.query_db("SELECT * FROM email_addresses")
        print emails
        return render_template('success.html', all_emails=emails)
    return redirect('/')

@app.route('/success', methods=['POST'])
def success():
        return render_template('success.html')

app.run(debug=True)
