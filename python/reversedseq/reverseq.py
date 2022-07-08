#crear una funcion que reciba un valor y cree una lista desde el valor hasta 0

def reversed_seq(n):
    rev = list(range(0,n+1))
    result =[]
    for i in reversed(rev):
        result.append(i)
    return result


# otra solucion es 
# def reversed_seq(n):
#     return list(range(n, 0, -1))

print(reversed_seq(10))
