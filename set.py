#1. 
s1 = {"C", "C++", "Python", "Java", "JavaScript", "C#", "Pascal", "R"}
print(s1)
#2, 3. 
s2 = {"Asmi Dagar", "20 years", "Female", "CS-23411203", "asmi.dagar.cs27@iilm.edu"}
print(s2)
print(type(s2))
#4. 
thisset = {"Java", "Python", "Django"}
if "Python" in thisset:
    print("Python is present")
else:
    print("Not present")
#5.
thisset1 = {"Java", "Python", "SQL"}
secondset = {"C", "Cpp", "NoSQL"}
thisset1.update(secondset)
print(thisset1)
#6.
thisset2 = {"Python", "Django", "JavaScript"}
myList = ["Java", "C"]
thisset2.update(myList)
print(thisset2)
#7. 
Set = {"Python", "Django", "JavaScript", "SQL"}
Set.pop()
print(Set)
#8.
Set1 = {"Python", "Django", "JavaScript", "SQL"}
Set1.clear()
print(Set1)
#9.
Set2 = {"Python", "Django", "JavaScript", "SQL"}
for i in Set2:
    print(i, end = "\t")
#10.
num = {10, 12,7, 8, 67, 90, 4, 5}
print()
print(min(num))
print(max(num))