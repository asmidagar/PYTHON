import functools

l1 = [1, 2, 3, 4, 5]

'''def fact(a, b):
    return a*b'''

ans = functools.reduce(lambda a, b: a*b, l1)
print(ans)