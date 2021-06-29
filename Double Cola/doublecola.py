names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 1

def who_is_next(names, r):
   
    count = (r**r) -1
    turn = names[count]
    print (turn)
    names = names.append(turn)
    
print (names)
    
minext = who_is_next(names, r)
print(minext)
