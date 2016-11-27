# students is a list [] of dictionaries {}
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# works like "for each dictionary item in the students list"
for dictionary_items in students:
    print dictionary_items["first_name"], dictionary_items["last_name"]
