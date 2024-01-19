def unique_in_order(iterable):
    list_final = list(iterable)
    result = set(list_final)
    return sorted(result)



print(unique_in_order('AAAABBBCCDAABBB'))
