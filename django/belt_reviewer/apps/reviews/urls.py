from django.conf.urls import url
from . import views
# from django.contrib import admin

app_name = "reviews"

urlpatterns = [
    # -----------------------------------
    # index: Display all books
    # Retrieve all books	GET	/books	index
    url(r'^$', views.index, name="index"),
    # -----------------------------------

    # new: Display a form to create a new product
    # Create a new pet	POST	/pets	create
    url(r'^new/$', views.new, name="new"),
    # <a href="new/">Add Book and Review</a>
    # calls create method
    #   <form action='/reviews/create' method='POST' >
    # -----------------------------------

    # create: Process information to create a new product
    # Create a new book	POST	/pets	create
    # called by <form action='/reviews/create' method='POST' >
    # creates new book and a review for the book
    url(r'^create$', views.create, name="create"),
    # -----------------------------------


    # show: Display a particular product
    # Display specific book	GET	/pets/<id>	show
    url(r'^showbook/(?P<id>\d+)', views.showbook, name="showbook"),
    # url(r'^showbook/(?P<id>\d+)', views.showbook, name="showbook"),

    # url(r'^showbook/(?P<id>\d+)$', views.showbook, name="showbook"),


    # -----------------------------------
    # url(r'^add_review/$', views.add, name="add_review"),
    # url(r'^register$', views.register, name="register"),
    # url(r'^show$', views.show, name="show"),
    # url(r'^success$', views.success, name="success"),
    # url(r'^show/(?P<id>\d+)/delete$', views.destroy, name="destroy"),
    # url(r'^login$', views.login, name="login"),
    # url(r'^admin/', admin.site.urls),
]

# Create 7 methods in your view/controller; refer to the routes in the wireframe for guidance
# index: Display all products url(r'^$', views.index, name="index"),

# show: Display a particular product
# new: Display a form to create a new product
# edit: Display a form to update a product
# create: Process information to create a new product
# update: Process information from the edit form and update the particular product
# destroy: Remove a product

# Using pets as an example resource:
#
# Action	HTTP Verb	Route Path	Function
# Retrieve all pets	GET	/pets	index
# Display form to create a new pet	GET	/pets/new	new
# Create a new pet	POST	/pets	create
# Display specific pet	GET	/pets/<id>	show
# Display form to update a specific pet	GET	/pets/<id>/edit	edit
# Update a specific pet	PUT or PATCH	/pets/<id>	update
# Delete a specific pet	DELETE	/pets/<id>	destroy
# For semi-RESTful architecture, you can append a /destroy to the destroy route.
