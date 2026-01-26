#PART-I
#1.
def func():
    print("TasinNCoder")

func()
#2.
def func1(a ,b):
    print(a)
    print(b)

str1 = "Asmi Dagar"
str2 = "CS-23411203"
func1(str1, str2)
#3.
def func2(*args):
    for item in args:
        print(item)

func2(10, 20, 30, 40)
#4.
def func3(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

func3(name="Asmi Dagar", age=20, city="Delhi")
#5.
def func4(list1):
    print(list1)

list1 = [10, 45, 78, 90]
func4(list1)
#6.
def max_num(a, b, c, d):
    Max = max(a, b)
    Max1 = max(Max, c)
    Max2 = max(Max1, d)
    print(Max2)

a = 10
b = 78
c = 45
d = 56
max_num(a, b, c, d)
#7.
def sum_list(list2):
    sum1 = sum(list2)
    print(sum1)

list2 = [12, 44, 34, 90]
sum_list(list2)
#8.
def mul_list(num):
    res = 1
    for num1 in num:
        res *= num1
    return res

list3 = [2, 3, 4, 5]

print(mul_list(list3))
#9.
def check_range(num, start, end):
    if start <= num <= end:
        return "Number is in the range"
    else:
        return "Number is not in the range"

number = 7
start = 1
end = 10

print(check_range(number, start, end))
#10.
def even_odd(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

num = int(input("Enter a number: "))
even_odd(num)

#PART-II
#1.
def unique_list(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5]

print(unique_list(numbers))
#2.
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = 7

if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")
#3.
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print_even_numbers(numbers)
#4.
def is_palindrome(text):
    return text == text[::-1]

string = "madam"

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")
#5.
def find_min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

print(find_min(10, 5, 8))
#6.
def square_list():
    squares = []
    for i in range(1, 31):
        squares.append(i * i)
    return squares

print(square_list())
#7.
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()   # calling inner function

outer_function()
#8.
def count_upper_lower(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

string = "Hello World"
count_upper_lower(string)
#9.
def is_pangram(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if char not in text:
            return False
    return True

string = "The quick brown fox jumps over the lazy dog"

if is_pangram(string):
    print("Pangram")
else:
    print("Not a Pangram")
#10.
def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"

if is_anagram(string1, string2):
    print("Anagram")
else:
    print("Not an Anagram")








