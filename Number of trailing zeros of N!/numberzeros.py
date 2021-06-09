""" 
Write a program that will calculate the number of trailing zeros in a factorial of a given number.


 """
from math import factorial

n = 1000   

def zeros(n):
     
  if n <= 0:
      return 0  
  elif n >= 1:
    numbers = list(str(factorial (n)))
    counter = 0 
    for num in reversed(numbers):
        if num == '0':
            counter += 1
        else:
            break 
  return counter      

mizeros = zeros(n)
print(mizeros)

