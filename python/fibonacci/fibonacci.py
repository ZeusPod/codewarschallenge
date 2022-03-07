n = 9

def fib(n):
    a = 0
    b = 1
    
    if n < 0:
        print("Incorrect input your number is negative")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else: 
        for i in range(1,n):
            c = a + b
            a = b 
            b = c
        return b 

me_fibo = fib(9)
print (me_fibo)