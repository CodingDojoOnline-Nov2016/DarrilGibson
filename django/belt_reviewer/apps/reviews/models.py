from __future__ import unicode_literals

from django.db import models
from .. loginreg.models import User

class BookManager(models.Manager):
    def add_book(self, data, user_id):
        print "in UserManager add_book"
        print data
        errors = []
        title = data['title']
        author = data['author']
        review_text = data['review']
        print data['rating']
        review_rating = int(data['rating'])
        print review_rating
        if len(title) == 0:
            errors.append("Please enter a title.")
        elif len(title) < 3:
            errors.append("Please enter a valid title.")

        if len(author) == 0:
            errors.append("Please select or enter an author's name.")
        elif len(author) < 3:
            errors.append("Please enter a valid author name.")

        if len(review_text) == 0:
            errors.append("Please enter a review.")
        elif len(review_text) < 4:
            errors.append("Please enter more for your review.")

        if review_rating == 0:
            errors.append("Please select a rating.")

        if errors:
            print errors
            return(False, errors)
        else: #No errors. Write book to database
            reviewing_user = User.objects.get(id=user_id)
            # reviewing_user = User.objects.get(id=user_id)
            # print reviewing_user
            # Add to parent table first
            newbook =self.create(title=title,author=author)
            book_id = newbook.id
            print book_id
            newbook.save()
            # After book is added, add data to child table
            bookreview=Review.objects.add_review(review_text, review_rating, reviewing_user, newbook)
            errors = []
            return (True, book_id)
        return book

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
    # Hidden from Review FK related_name= "reviews"
	# reviews

class ReviewManager(models.Manager):
    def add_review(self, review_text, review_rating, reviewing_user, reviewed_book):
        action =self.create(review_text=review_text, review_rating=review_rating, reviewing_user=reviewing_user, reviewed_book=reviewed_book)
        action.save()
        return (True)

# FK points to User in loginreg app
class Review(models.Model):
    review_text = models.CharField(max_length=2500)
    review_rating = models.PositiveSmallIntegerField()
    reviewed_book = models.ForeignKey(Book, related_name="reviews")
    reviewing_user = models.ForeignKey(User, related_name="user_review")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()
