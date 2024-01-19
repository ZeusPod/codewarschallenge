from collections import Counter

def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())


print(is_anagram("apple", "pale"))
print(is_anagram("foefet", "toffee"))
