#LIST
l1.insert(-9, 70)
print(l1)

a,b,c = [1,2,3]
l1 = a,b,c

print(a,b,c)
print(l1)

data =l1.pop()
print(data)
print(l1)

data = l1.remove(30)
print(data)
print(l1)

print(l1.count(45))
print(l1.count(30))

l1[2] = 30
print(l1)

#l1.sort()
l1.sort(reverse=True)
print(l1)

l1 = [_*_ for _ in l1]
print(l1)

#RANGE
num = int(input("Enter a number: "))
for i in range(num):
    print(i+1, end = "\t")

for i in range(1, num, 2):
    print(i, end = "\t")

l1 = [2, 45, 88, 66, 89]

#STR
name = "Asmi Dagar"
print(name)

for _ in name:
    print(_, end=" ")
print()

print(name[2:8])
print(name[-8:-1])

s = "12 345 56 457"
l1 = s.split(" ")
print(l1)
print(s)

