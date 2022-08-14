#write a function that returns ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    list_result = [str(lines.index(x) + 1) + ": " + x for x in lines ]
    return list_result

print(number(["a", "b", "c"]))