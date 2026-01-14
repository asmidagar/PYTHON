#import keyword
#from keyword import kwlist, softkwlist
#from keyword import *
#from keyword import kwlist as list

'''print(keyword.kwlist)
print()
print(keyword.softkwlist)'''

#print(list)
#print()
#print(softkwlist)

#WAp whether a given no is +ve, -ve or zero
'''n = int(input("Enter number to check "))
if(n < 0):
    print("Number is -ve")
elif(n > 0):
    print("Number is +ve")
else:
    print("Number is zero")'''

year = int(input("Enter year "))
if(year % 100 == 0):
    if(year % 400 == 0 ):
        print("Leap Year")
    else:
        print("Not Leap year")
else:
    if(year % 4 == 0):
        print("Leap year")
    else:
        print("Not leap year")