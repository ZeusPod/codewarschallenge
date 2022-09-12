from collections import Counter

def delete_nth(order,max_e):
    result=[]
    for x in order:
        if result.count(x) < max_e:
            result.append(x)

    return result
     
    

print(delete_nth([20,37,20,21], 1))
