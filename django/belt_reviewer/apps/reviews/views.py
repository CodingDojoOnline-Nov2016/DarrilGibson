from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from . models import Review, Book

# Added notes on semi-RESTful methods

# -------------------------------------
# index: Display all books and reviews - Get
# Retrieve all books and reviews	GET	/pets	index
# This will need a template.
# @app.route('/users')
# def users():
#     return redirect('/')
def index(request):
    print "in reviews:index"
    print request.session['firstname']
    if 'firstname' in request.session:
        # print request.session['name']
        messages.info(request, "Welcome")
    else:
        messages.info(request, "Not logged in")
    context = {
        "books": Book.objects.all()
        }
    return render(request, 'reviews/index.html', context)

# -------------------------------------
# new: Display a form to create a new book and reviews
# Display form to create a new book and review	GET	/pets/new	new
# This will need a template.
# @app.route('/users/new')
# def new():
#     return render_template('new.html')
def new(request):
    return render(request, "reviews/new.html")

# -------------------------------------
# create: Process information to create a new product
# Create a new book	POST	/pets	create
# @app.route('/users/create', methods=['POST'])
# def create():
#     errors=[]

def create(request):
    if request.method == "POST":
        print "in create"
        print request
        request.session['title'] = request.POST['title']
        print request.session['title']
        request.session['author'] = request.POST['author']
        request.session['review'] = request.POST['review']
        # request.session['rating'] = request.POST['rating']
        success, book_manager_response = Book.objects.add_book(request.POST, request.session['user_id'])
        print book_manager_response
        if success: # book Added
            # print "success book added"
            msg = "This book has been successfully added."
            messages.success(request, msg)
            book_id = book_manager_response
            # return redirect('showbook', book_id)
            return redirect(reverse('reviews:showbook', kwargs={'id': book_id}))
        else: # errors
            for error in book_manager_response:
                messages.error(request, error)
            return render(request, "reviews/new.html")
    else: #request.method != POST
        return render(request, "reviews/index.html")
    return render(request, "reviews/index.html")    #tmp

def showbook(request, id):
    if request.method == "POST":
        print "in showbook"
        book = Book.objects.get(id=id)
        print book
        context = {
            "books": books
        }
        return render(request, "reviews/showbook.html", context)
    else: #request.method != POST
        return redirect("new")
# Create 7 methods in your view/controller; refer to the routes in the wireframe for guidance
# index: Display all products
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





# show: Display a single book and reviews
# Display specific pet	GET	/pets/<id>	show
# This will need a template.
# @app.route('/users/<id>')
# def show(id):
#     data = {'id': id}
#     select_query = ('SELECT id, first_name, last_name, email, created_at FROM users WHERE id=:id')
#     user = mysql.query_db(select_query, data)
#     return render_template('show.html', user=user)
# def show(request):
#     return render(request, "reviews/new.html")
#
# def create(request):
#     if request.method == "POST":
#         print "in create"
#         print request
#         return render(request, "reviews/new.html")
#     else: #request.method != POST
#         return render(request, "reviews/index.html")
#     return render(request, "reviews/index.html")    #tmp


# -------------------------------------
# edit: Display a form to update a book
# Display specific pet	GET	/pets/<id>	show
# This will need a template.
# @app.route('/users/<id>/edit')
# def edit(id):
#     data = {'id': id}
#     select_query = ('SELECT id, first_name, last_name, email FROM users WHERE id=:id')
#     user = mysql.query_db(select_query, data)
#     return render_template('edit.html', user=user, id=id)

# -------------------------------------
# update: Process information from the edit form and update the particular product
# Update a specific pet	PUT or PATCH	/pets/<id>	update
# @app.route('/users/<id>', methods=['POST'])
# def update(id):
#     data = {'id': id}
#     # Compare to create method
#     errors=[]

# -------------------------------------
# destroy: Remove a product
# Delete a specific pet	DELETE	/pets/<id>	destroy
# @app.route('/users/<id>/destroy')
# def destroy(id):
#     data = {'id': id}
#     delete_query = ('DELETE FROM users WHERE id =:id')
#     result_comments = mysql.query_db(delete_query, data)
#     return redirect('/')

# -------------------------------------




# def addbook(request):
#     return render(request, 'reviews/addbook.html')
#
# def addreview(request):
#     return render(request, 'reviews/addreview.html')
