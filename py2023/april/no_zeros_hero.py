def no_boring_zeros(n):
    return 0 if n == 0 else int(str(n).rstrip('0'))
    



print(no_boring_zeros(1450))
