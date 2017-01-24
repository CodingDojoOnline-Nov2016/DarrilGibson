from __future__ import unicode_literals
from django.db import models
# Email regex pattern
import re
regex_pattern=r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$'

# Manager for User class
class UserManager(models.Manager):
    def register(self, email):
        # Called by email_check = User.objects.register(request.POST['email'])
        print email
        errors = []
        if len(email) == 0:
            errors.append("Please enter an email address.")
        elif not re.match(regex_pattern,email):
            errors.append("Please enter a valid email address.")
        else: # check for address in database already
            try:
                # If this succeeds, it indicates email address already in database
                action = User.objects.get(email=email)
                errors.append("Sorry, but that email address already exists in the database. Please enter a different email address.")
            except Exception as e:
                pass
        if errors:
            print errors
            return (False, errors)
        else: # No errors write email to database
            action = self.create(email=email)
            action.save()
            return (True, action)

    def deleteuser(self, id):
        obj = self.get(id=id)
        obj.delete()

class User(models.Model):
    # Project only needs email and time stamps, but that isn't realistic for an actual table
    # Other fields will be needed in typical app
    # first_name = models.CharField(max_length=45)
    # last_name = models.CharField(max_length=45)
    # password = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Connect UserManager to User class to add methods
    objects = UserManager()
