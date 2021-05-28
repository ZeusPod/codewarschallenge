def solution (number):
    sum = 0
    for num in range(number):
        if num % 3 == 0:
            sum = sum + num
        elif num % 5 == 0:
            sum = sum + num
    else:
        return sum


number = 10
mi_suma = solution(number)
print (mi_suma)