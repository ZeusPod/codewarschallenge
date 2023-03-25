import re 

def reverse_letter(string):
   str = re.sub(r'[a-zA-Z]', '', string)
   return str[::-1]    

print(reverse_letter("_"))
