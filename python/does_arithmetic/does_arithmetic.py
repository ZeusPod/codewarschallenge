def arithmetic(a,b,operator):
    if operator == "add":
        return int(a + b) 
    elif operator == "subtract":
        return int(a - b) 
    elif operator == "multiply":
        return int(a * b) 
    else: 
        return (a / b) 

    

print (arithmetic(8,4,'add'))

