# bubble sort low to high
# base case [3,1,5,9,7]
# set int_num1 to be first number
# set int_num2 to be second number
# if intnum1 > intnum2, swap
# repeat
a = [3,1,5,9,7]

for count in range (0, len(a)-1 ):
    int_num1 = a[count]
    int_num2 = a[count+1]
    if a[count] > a[count+1]:
        a[count] = int_num2
        a[count+1] =  int_num1
print a
