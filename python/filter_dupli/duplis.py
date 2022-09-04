
def remove_duplicates(arr)->list:
    no_duplicates=[]
    for i in arr:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates

arr=[1,5,1,3,2,1,5,1,9,8,7,6,3]

print(remove_duplicates(arr))



