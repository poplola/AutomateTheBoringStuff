# output ==> [1, 2, 3, 7, 8, 5, 6]

def reduce(arr):
    combineArr = []
    for element in arr:
        combineArr += element
    return combineArr

myArr = [[1, 2, 3], [7, 8], [5, 6]]
print(reduce(myArr))