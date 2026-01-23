def fun(s, t):
    slen = len(s)
    tlen = len(t)
    if slen != tlen:
        return False
    
    l1 = []
    for _ in range(26):
        l1.append(0)

    for index in range(slen):
        l1[ord(s[index]) - 97] += 1
        l1[ord(t[index]) - 97] -= 1

    for v in l1:
        if v != 0:
            return False
        
    return True

s = "aaabb"
t = "abab"
t = fun(s, t)
if t == True:
    print("Valid Anagram")
else:
    print("Not a valid Anagram")