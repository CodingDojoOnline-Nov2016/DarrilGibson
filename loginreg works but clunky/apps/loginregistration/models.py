from __future__ import unicode_literals
from django.db import models
import bcrypt

# Email name regex patterns
import re
regex_email=r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$'
#instructions say letters only for name
regex_name= r'^[a-zA-Z]*$'

class UserManager(models.Manager):
    def register (self, first_name, last_name, password, cpassword, email):
        errors = []
        if len(first_name) < 3:
            errors.append("Please enter your first name.")
        elif not re.match(regex_name,first_name):
            errors.append("Please enter only letters in your first name.")

        if len(last_name) < 3:
            errors.append("Please enter your last name.")
        elif not re.match(regex_name,last_name):
            errors.append("Please enter only letters in your last name.")

        if len(email) == 0:
            errors.append("Please enter your email address.")
        elif not re.match(regex_email,email):
            errors.append("Please enter a valid email address.")
        else:
            if User.objects.filter(email=email).exists():
            # duplicate_email_check
                errors.append("That email address already exists in the database. Please enter a different email address.")

        if len(password) < 8:
            errors.append("Your password must be at least 8 characters long.")
        elif password != cpassword:
            errors.append("Your passwords don't match.")
        else:
            pw = password.encode()
            hashpassword = bcrypt.hashpw(pw,bcrypt.gensalt())

        if errors:
            print "in user manager"
            print errors
            # request.session['errors'] = errors
            return(False, errors)
        else: #No errors. Write user to database
            action =self.create(first_name=first_name,last_name=last_name,email=email,password=hashpassword)
            action.save()
            errors = []
            return (True,errors)

    def login (self, email, password):
        # check for email first
        if User.objects.filter(email=email).exists(): # email is in database
            user = User.objects.get(email=email) # Get user object
            userpw = user.password.encode() # stored password for user
            provided_pw = password.encode()
            if bcrypt.hashpw(provided_pw, userpw) == userpw:
                print "passwords match"
                return (True)
            else:
                return (False)
        else: # email doesn't exist
            return (False)

    def deleteuser (self, id):
        action = self.get(id=id)
        action.delete()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    # birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Connect UserManager to User class to add methods
    objects = UserManager()
