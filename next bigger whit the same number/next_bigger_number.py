""" Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
 """

num = int(input("Please enter a positive integer: "))

def next_bigger(num):
    num_list = []
    num_list = list(str(num))
    if len(num_list) == 1:
        return -1
    elif len(num_list) == 2:
        if num_list[0] < num_list[1]:
            return int(''.join(num_list[::-1]))
        else:
            return -1
    

print(next_bigger(num))

