""" Given an array of integers, find the one that appears an odd number of times. """

#def function

def find_int(seq):
    number_dict = []
    for i in seq:
        if seq.count(i) % 2 != 0:
           number_dict.append(i)

    return max(number_dict)


print(find_int([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


