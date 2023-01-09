list1=[1,2,3,4,5,6,7,8,9,10]

def even_odd(n:int):
    if n % 2 == 0:
        print(n,'is even')
    else:
        print(n,'is odd')

result= list(map(even_odd, list1))

