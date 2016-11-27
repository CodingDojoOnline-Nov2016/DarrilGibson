# Part 1
def draw_stars(input_list):
    for count in range (0,len(input_list) ):
        stars = ""
        # for i in range (1, input_list[count]):
        for starscount in range (1, input_list[count]+1):
            stars = stars + "*"
        print stars
x = [4,6,1,3,5,7,25]
draw_stars(x)

# Part 2
def draw_stars_2(input_list):
    for count in range (0,len(input_list) ):
        if type(input_list[count]).__name__ == 'str':
            # Get length of string
            str_length = len(input_list[count])
            # Get first character
            first_letter = (input_list[count][0])
            print_letter = (input_list[count][0])
            for letter_count in range (1, str_length):
                print_letter = print_letter + first_letter
            print print_letter
        elif type(input_list[count]).__name__ == 'int':
            print "Variable is a int."
            stars = ""
            for starscount in range (1, input_list[count]):
                stars = stars + "*"
            print stars
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_2(y)
