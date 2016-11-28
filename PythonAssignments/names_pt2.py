# Part 2
# users is a dictionary {} - Students and Instructors
# Students is a list [] of dictionaries {}
# Instructors is a list [] of dictionaries {}
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students"
# use int_count as counter for printout
int_count = 1
for dictionary in users['Students']:
    # Get first and last name of student and convert to list
    # The following line formats it as ['first_name','last_name']
    str_name = dictionary.values()
    # format name as first_name space last_name and store in str_full_name
    str_full_name = ""
    for count in range(0,2):
        str_full_name = str_full_name + " " + str_name[count]
        # str_full_name = str_full_name + " - " + str(len(str_full_name))
    #Get number of characters in name (-2 for added spaces)
    int_char_count = len(str_full_name) - 2
    print str(int_count) + " -" + str_full_name + " - " + str(int_char_count)
    int_count = int_count + 1

print "Instructors"

# use int_count as counter for printout
int_count = 1
for dictionary in users['Instructors']:
    # Get first and last name of instructor and convert to list
    # The following line formats it as ['first_name','last_name']
    str_name = dictionary.values()
    # format name as first_name space last_name and store in str_full_name
    str_full_name = ""
    for count in range(0,2):
        str_full_name = str_full_name + " " + str_name[count]
        # str_full_name = str_full_name + " - " + str(len(str_full_name))
    #Get number of characters in name (-2 for added spaces)
    int_char_count = len(str_full_name) - 2
    print str(int_count) + " -" + str_full_name + " - " + str(int_char_count)
    int_count = int_count + 1
