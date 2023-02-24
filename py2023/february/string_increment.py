def string_increment(strng):
    list_word = list(strng)
    numbers = [x for x in list_word if x.isnumeric()]
    worses = [x for x in list_word if x.isalpha()]
    print(worses)
    if len(numbers) == 0:
        list_word.append('1')

        return "".join(list_word)
    else:
        num =int("".join(numbers))
        return ''.join(worses) + str(num + 1)  


print(string_increment('foobar23'))


