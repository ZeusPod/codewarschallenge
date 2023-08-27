def anagram(test:str, original:str)-> bool:
    list1 = list(test)
    list2 = list(original)
    for w in list1:
        if w in list2:
            list2.remove(w)

    if len(list2) == 0:
        return True
    else:
        return False

 
print(anagram('jose', 's2je'))


