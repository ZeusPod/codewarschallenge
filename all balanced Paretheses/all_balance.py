""" Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses """

def balanced_parens(n):
    list_parens = []
    if n == 0:
        list_parens.append("")
    for i in range(n):
        for left in balanced_parens(i):
            for right in balanced_parens(n-1-i):
                list_parens.append("(" + left + ")" + right)

    return list_parens


n = 3

print(balanced_parens(n))

