""" Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

 """

def unique_in_order(iterable):
    text1 = list(iterable)
    textfilter = []
    for c in text1:
        if c not in textfilter:
            textfilter.append(c)
    return(textfilter)

text = "abzzzedmdltt"

mi_order = unique_in_order(text)
print(mi_order)
