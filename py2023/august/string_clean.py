import doctest
import re

def string_clean(s):
    """
    funcition will return the cleaned string without numbers
    """
    num = re.findall('\d+', s)
    return num


print(string_clean("ho9la"))
