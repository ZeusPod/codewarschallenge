
x = ["Ryan", "Jimmy", "123", "4", "Cool Man"]

def friend(x):
    should = []
    for name in x:
        if len(name) == 4:
            should.append(name)
    return(should) 

me_friends = friend(x)
print (me_friends)