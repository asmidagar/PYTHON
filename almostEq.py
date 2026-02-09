#Leetcode 1790
def areAlmostEqual(s1, s2):
    count = 0
    f = s = None

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:
            count += 1
            s = f
            f = i
        if count > 2:
            return False
        
    if f == None and s == None:
        return True
    if s == None:
        return False
    if s1[f] == s2[s] and s2[s] == s1[f]:
        return True
    
s1 = "kelb"
s2 = "kelb"
a = areAlmostEqual(s1, s2)
if a == True:
    print("True")
else:
    print("False")