# num 1-5, 1->monday, 5->friday
num = int(input("Enter a number: "))
match(num) :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Holiday") 
