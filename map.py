l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f1(x):
    return x*x

def f1(x):
    if(x % 2 == 0):
        return x*x
    
    return x**4

ans = map(f1, l1)
for val in ans:
    print(val, end = "\t")

print()