def playin_banjo(str):
    low = str.lower()
    low.split()
    if low[0] == 'r':
        return f"{str} plays banjo"
    else:
        return f"{str} does not play banjo"

print(playin_banjo('Jose Morales'))
