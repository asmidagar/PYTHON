#1, 2, 3, 4, 5.
d = {"Name" : "Asmi Dagar", "Age" : 20, "Gender": "Female", "Roll-No" : "CS-23411203"}
print(d)
print(d["Gender"])
List = list(d.values())
print(List)
d['Age'] = 22
print(d)
List1 = d.keys()
for i in List1:
    print(i, end= "\t")
    print()
#6. 
nested_dict = {
    "student1": {
        "name": "Asmi Dagar",
        "age": 20
    },
    "student2": {
        "name": "Archi Kumari",
        "age": 21
    },
    "student3": {
        "name": "Riha Singh",
        "age": 21
    }
}

print(nested_dict)
#7. 
dict1 = {
    "name": "Asmi Dagar"
}

dict2 = {
    "name": "Archi Kumari"
}

dict3 = {
    "name": "Riha Singh"
}

main_dict = {
    "dict1": dict1,
    "dict2": dict2,
    "dict3": dict3
}

print(main_dict)
#8. 
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

result = dict(zip(list1, list2))

print(result)
#9.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)

print(dict1)
#10.
sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

lowest_key = min(sample_dict, key=sample_dict.get)

print(lowest_key)
