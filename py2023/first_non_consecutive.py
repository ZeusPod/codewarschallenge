"""
Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array."""



def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != 1:
            return arr[i]


first = first_non_consecutive([1,2,8,3,4,5,6])
print(first)
