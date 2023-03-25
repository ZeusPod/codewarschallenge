import re

def order(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=lambda x: int(re.findall(r'\d+', x)[0]))
    return ' '.join(sorted_words)

print(order("is2 Thi1s T4est 3a"))
