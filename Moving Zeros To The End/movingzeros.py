""" Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

 """

def move_zeros(array):
    count = len(array)
    newarray = []
    for i in array:
        if i != 0:
            newarray.append(i)
    count2 = count - len(newarray) 
    while count2 >= 1:
        newarray.append(0)
        count2 -= 1
    return newarray

array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

me_moving = move_zeros(array)
print(me_moving)