""" Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

 """
string = "Hey fellow warriors"

def spin_words(string):
        order = list(string)
        order.reverse()
        new_rev = "".join(order)
        return new_rev


me_reverse = spin_words(string)
print(me_reverse)