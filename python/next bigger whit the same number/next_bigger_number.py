""" Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
 """

def next_bigger(num):
    numbers=str(num)
    numbers.split()
    list_numbers=[]
    for n in numbers:
        if len(list_numbers)==0:
            list_numbers.append(n)
        elif n > list_numbers[0]:
            list_numbers.insert(0,n)
        else: 
            list_numbers.append(n)
    fn=''.join(list_numbers)
    return int(fn)

print(next_bigger(2017))

    
        

