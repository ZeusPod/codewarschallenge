
integers = [2, 4, 6, 8, 10, 3]
#integers = [2, 4, 0, 100, 4, 11, 2602, 36]
#integers = [160, 3, 1719, 19, 11, 13, -21]



def find_outlier(integers):
    par = []
    impar = []
  
    for elements in integers:
        #contamos que opcion es mayor
        if elements % 2 == 0:
           par.append(elements)
        else:
           impar.append(elements)
    if len(par) > len(impar):
        return(impar[0])
    else:
        return(par[0])

me_elements = find_outlier(integers)
print(me_elements)

