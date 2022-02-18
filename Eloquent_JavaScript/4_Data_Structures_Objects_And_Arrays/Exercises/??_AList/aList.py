
# ?? result ==> [1, [2, [3, null]]]

def listOfMyArr(arr):
    print(arr)
    myList = []
    for i in range(len(arr)):
        print(arr[i])
        myList.append(arr[i:])
        # myList.append(listOfMyArr(arr[i:]))

    return myList

myArr = [1,2,3]
print(listOfMyArr(myArr))