def solve(s):
  list_s = list(s)
    upper , lower = 0, 0 
    for l in list_s:
        if l.islower():
            lower +=1 
        else:
            upper +=1
    if lower > upper or lower == upper:
        return s.lower()
    else:
        return s.upper() 
