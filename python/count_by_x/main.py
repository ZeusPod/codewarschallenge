def count_by(x, n):
    if x > n:
        my_list = [*range(n, x + 1 , 2)]
        return my_list
    else:
        my_list = [*range(x, n + 1, 2)]
        return my_list


print(count_by(2, 5))