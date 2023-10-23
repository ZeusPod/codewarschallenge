from typing import List


def accum(s):
   accum = list(s)
   list_new = []
   x = 0
   for a in accum:
       list_new.append((a * x) + '-')
       x +=1 
   capi = [x.capitalize() for x in list_new]
   
   return "".join(capi)

print(accum('abcd'))
   
