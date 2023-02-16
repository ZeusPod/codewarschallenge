
def duplicate_count(text):
    textfinal = list(text.lower())
    norepeat = set(textfinal) 
    
    contador = 0
    for n in norepeat:
        count = textfinal.count(n)
        if count > 1:
            contador += 1 

    return contador
    



