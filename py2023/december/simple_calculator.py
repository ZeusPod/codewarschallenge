def calculator(x,y,op):

    def sum(x,y):
        return sum(x,y)

    def sub(x,y):
        return x - y

    def div(x,y):
        return x / y 

    def mult(x,y):
        return x * y if x > 0 and y > 0 else 0 

    operators={
            
            '+': sum ,
            '-': sub,
            '*': div,
            '/': mult 

            }

    operation_func = operators.get(op)
    
    if operation_func: 
        return operation_func(x,y)
    else:
        return "Operador no valido"


print(calculator(4,2,'-'))
