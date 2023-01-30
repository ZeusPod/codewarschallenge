def conuntByX(a, b):
    r = range(b+1)
    result =[] 
    for i in r:
       if i > 0:
           result.append(i*a)
    return result

print(conuntByX(2,5))
