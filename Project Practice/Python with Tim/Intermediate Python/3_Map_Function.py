#3 Map Function
# apply function in the item of list to create a new list

# <===== Practice 1: orginal thinking of solution  =====>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x

newList = []
for x in li:
    newList.append(func(x))

print(" #1: ", newList)


# <===== Practice 2: use map function  =====>
print(" #2: ", list(map(func, li)))

# <===== Practice 3: comprehension =====>
print(" #3: ", [func(x) for x in li ])

# <===== Practice 4: comprehension + expression =====>
print(" #4: ", [func(x) for x in li if x%2 == 0])
