""" Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences. """
from heapq import nlargest
import re


text1 = ("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")

text = "  '  "


def top_3_words(text):

    text1 = text.lower()
    list1 = re.sub('[^\'\"a-zA-Z0-9]',' ',text1)
    milist = list1.split()
    word_freq = {}

    for w in milist:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1
    final_list = nlargest(3, word_freq, key=word_freq.get)
    return final_list


most_word = top_3_words(text)
print(most_word)
