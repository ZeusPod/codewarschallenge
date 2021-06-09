s = ('djksmowjddksjjdh')

def solution(s):
    list1 = []
    for i in range(len(s)):
        if len(s) % 2 != 0:
            s = s + "_"
            print(s)
        if i % 2 == 0:
            list1.append(s[i:i + 2])

    return list1


me_solution = solution(s)
print(me_solution)
