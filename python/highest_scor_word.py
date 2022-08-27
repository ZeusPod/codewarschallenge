# crear una funcion que cuente las letras de cada palabra y segun su puntuja devuelva la
# mayor tomar en consideracion que cada una tendra el valor de su posicion en el alfabeto
# es decir ejemplo a =1 , b =2 y asi sucesivamente
from string import ascii_lowercase


def highest_score(x):
    alfabeto =[]
    [alfabeto.append(x) for x in ascii_lowercase]
    dic_alf ={}
    position = 1
    for a in alfabeto:
        dic_alf[a]= position
        position +=1
    worse=list(x)
    split_worse = []
    for w in worse:
        split_worse.append(w.split)


        
    return(split_worse)

print(highest_score("ahora si vamos a probar"))



