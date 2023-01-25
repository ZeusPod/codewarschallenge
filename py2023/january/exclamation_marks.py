def replace_exclamation(s):
    vocals=["a","e","i","o","u"]
    result=[]
    for x in list(s):
        result.append(x) if x not in vocals else result.append("!")
    return "".join(result)
    


print(replace_exclamation('Hi!'))
