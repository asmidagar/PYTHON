#leetcode26
#1
l1 = [0, 0, 1, 2, 3, 3, 3, 4, 5, 5, 5]
print(l1)
x = 1
r = []
r.append(l1[0])
c = 0
while x < len(l1):
    if(r[c] != l1[x]):
        r.append(l1[x])
        c += 1
    x += 1

print(r)

#2
l1 = [0, 1, 2, 3, 3, 3, 3]
print(l1)
c = 0
x = 1
while x < len(l1):
    if l1[c] != l1[x]:
        c += 1
        l1[c] = l1[x]
    x += 1

print(l1[0:c+1])