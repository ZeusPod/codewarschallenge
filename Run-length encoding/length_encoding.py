def run_length_encoding(s):
    if s == "":
        return []
    
    count = 1
    prev = s[0]
    rle = []
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            rle.append([count, prev])
            prev = s[i]
            count = 1
    rle.append([count, prev])
    return rle

print(run_length_encoding("abc"))
