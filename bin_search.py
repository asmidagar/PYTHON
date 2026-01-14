list1 = [10, 12, 20, 25, 30, 45, 60, 70]
target = int(input("Enter element to search"))
left = 0
right = len(list1) - 1

def bin_search(x, left, right):
    mid = (left + right) // 2

    if(list1[mid] == x):
        print("Element found")
    elif(list1[mid] < x):
        bin_search(x, left+1, right)
    elif(list1[mid] > x):
        bin_search(x, left, right-1)
    
bin_search(target, left, right)
