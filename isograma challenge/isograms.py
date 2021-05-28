""" 
    Script para determinar si una cadena es un isograma(palabra en la cual no se repiten ninguna de las letras)

 """

def is_isogram(worse):
    worse = worse.lower()
    for char in worse:
        if worse.count(char) > 1:
            return print("Is not a isogram")
            
        else:
            return print("Is a isogram") 
               

worse = input("please tell me your worse: ")
list(worse)
me_isogram = is_isogram(worse)
print(me_isogram)