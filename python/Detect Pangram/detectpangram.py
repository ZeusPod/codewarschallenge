""" A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). """

import string

def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    for alphabet in s:
        if alphabet not in s:
            return False 
        elif len(s) < 27:
            return False
        
        else:
            return True
    
s = "The quick, brown fox jumps over the lazy dog!"
me_string = is_pangram(s)
print(me_string)

