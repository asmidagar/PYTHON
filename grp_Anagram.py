#Leetcode 49
def grpAnag(str):
    d = {}
    for i in str:
        data = ' '.join(sorted(i))
        if data in d:
            d[data].append(i)
        else:
            d[data] = [i]

    return list(d.values())

str = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
L = grpAnag(str)
print(L)