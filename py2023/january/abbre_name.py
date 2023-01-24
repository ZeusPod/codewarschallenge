def abbrev_name(name):
    list_name = name.split()
    list_result=[]
    iter = 0
    while iter < len(list_name):
        list_result.append(list_name[iter][0])
        iter +=1
        
    return '.'.join(list_result)
print(abbrev_name("Sam Harris"))
