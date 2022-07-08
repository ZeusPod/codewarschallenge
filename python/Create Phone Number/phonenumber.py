""" Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

 """


def create_phone_number(n):
    long = len(n)
    if long > 10:
        return False
    elif long < 10:
        return False
    #if long is ok proced to print in format
    elif long == 10:
        n = "".join(map(str, n))
        return "(" + n[0:3] + ")" + " " + n[3:6] + "-" + n[6:]


n = [1,2,3,4,5,6,7,8,9,0,]
mi_phone = create_phone_number(n)
print(mi_phone)
