def score_to_grade (score):
    if score <= 60:
        grade = 'F'
    elif score <= 70:
        grade = 'D'
    elif score <= 80:
        grade = 'C'
    elif score <= 90:
        grade = 'B'
    else:
        grade = 'A'
    return grade

print "Scores and Grades"
for count in range (1,11):
    print "What was the student's score?"
    input_score = raw_input()
    int_score = int(input_score)
    print "Score: " + input_score + "; Your grade is " + score_to_grade(int_score)

print "End of the program. Bye."
