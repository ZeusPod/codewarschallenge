def vowel_remover(str):
    worse = list(str)
    vocals = ['a','e','i','o','u']
    result = [x for x in worse if x not in vocals]
    return "".join(result)

print(vowel_remover('paralelepipedo'))
