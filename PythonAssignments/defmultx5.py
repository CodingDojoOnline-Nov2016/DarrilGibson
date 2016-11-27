def multx5 (list_in, multiplier):
    for count in range (0, len(list_in) ):
        list_in[count] = list_in[count] * multiplier
    return list_in
a = [2, 4, 10, 16]
b = multx5(a,5)
print b
