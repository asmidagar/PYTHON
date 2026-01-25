#1.
t1 = ("Java", "Python", "SQL", "C")
print(t1)
#2. 
t2 = ("Java",)
print(t2)
#3. 
T = t1[::-1]
print(T)
#4. 
t3 = (10, 20, 30)
t4 = ("Java", "Programming", "Languaga")
t3, t4 = t4, t3
print(t3)
print(t4)
#5.
t = (10, 10, 10, 10)
if t.count(t[0]) == len(t):
    print("Items are same")
else:
    print("Items are not same")
#6.
T1 = (100, 200, 300, 400)
a, b, c, d = T1
print(a, b, c, d, sep = " ")
#7.
tuple1 = (1, 2, 3, 4, 5, 6)
newT = tuple1[3:5]
print(newT)
#8.
tuple4 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
print(tuple(sorted(tuple4, key = lambda x: x[1])))
#9.
tuple2 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple2[1][1])
#10.
tuple3 = (11, [22, 33], 44, 55)
tuple3[1][0] = 66
print(tuple3) 