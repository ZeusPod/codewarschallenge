
def remove_duplicates(arr)->list:
    list_aux=set(arr)
    return list(list_aux)


arr=[1,5,1,3,2,1,5,1,9,8,7,6,3]

print(remove_duplicates(arr))



