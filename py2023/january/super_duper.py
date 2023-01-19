def problem(a):
    if isinstance(a,int) or isinstance(a,float):
        return int(a * 50 + 6)
    else:
        return "Error"



test1 = problem(1.2)
print(test1)
