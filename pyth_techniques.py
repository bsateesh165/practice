from collections import Counter


# # list_comprehension
# square = [i*i for i in range(10)]
# # print(square)

# # to remove negitive elements from a list instead of range we can use enumarate
# lis = [5, 4, -3, -2, 9, -1]
# for num, idx in enumerate(lis):
#     if num < 0:
#         lis.remove(num)

# print("enumarate", lis)



# # sorted
# data = [3, 4, 8, 9, 1, 10]
# sorted_data = sorted(data)
# # print(sorted_data)

# dic_data = [{"name": "sat", "age": 23},
#             {"name": "jim", "age": 21},
#             {"name": "sam", "age": 25}
# ]

# sorted_dic_data = sorted(dic_data, key=lambda x: x["age"])
# print(sorted_dic_data)

# # lambda is a ananomas function used for one time call with out function name only variable 
# # used for simple logics
# x = lambda x: x*x
# print(x(5))
# # we can call variable as function and provide avriable


# # get and setdefault for dictinary
# # counter is used to count the no of repeated elements in list

lis1 = [3,3,3,3,4,4,5,5,2,2,3,3,4,4,1]
count = Counter(lis1)
print(count[3])

most_common = count.most_common(1)
print(most_common)


# ternary_condition
# by using this we can write if else condition in one line
#Bad
condition = False

if condition:
    x = 1
else:
    x = 0
print(x)

# good
y = 1 if condition else 0
print(y)

# Zip
# it is used when we need loop more than one lists
value = ["name", "age", "height", "weight"] 
data1 = ["sateesh", 24, 5.9, 65]
# we can use no of lists
for var, val in zip(value, data1):
    print(f"{var}: {val}")


# fibonoci numbers
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for i in fib():
    if i > 100:
        break
    print(i)