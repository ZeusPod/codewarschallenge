def print_error(str):
    large = len(str)
    count = 0
    str.lower()
    list_str = list(str)
    compare = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']    
    for letter in list_str:
        if letter not in compare:
            count +=1 
    return f"{count}/{large}"

 

print(print_error("aaaaZZZZ"))
