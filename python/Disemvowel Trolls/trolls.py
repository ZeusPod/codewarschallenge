def disemvowel(string_):
    vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string2_ = []
    for i in string_:
        if i not in vocals:
            string2_.append(i)
    return ''.join(string2_)


