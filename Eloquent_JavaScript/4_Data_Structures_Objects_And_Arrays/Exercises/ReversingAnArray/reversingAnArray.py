def newArray():
    step = 1
    newArr = []
    for i in range (1, 11):
        newArr.append(i*step)
    return newArr

def reverseArray(arr):
    arr.reverse()
    return arr

print(newArray())
print(reverseArray(newArray()))