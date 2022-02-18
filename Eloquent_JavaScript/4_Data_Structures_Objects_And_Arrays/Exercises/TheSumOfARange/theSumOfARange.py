def newRange(start, end, step=1):
    newArray = []
    num = start
    print(f"({start}, {end}, {step}) ==> ", end='')

    if (step < 0 and start < end) or (step > 0 and start > end):
        return "Valid data! Can't create an array!"

    # for i in range(int(round(abs(start-end))/abs(step))+1):
    # if comprehension in while loop
    while num <= end if start <= end else num > end:
        newArray.append(num)
        num += step
    return newArray

def sumOfArray(arr):
    total = sum(arr)
    print(f"Sum of array {arr} is ", end="")
    return total
    


print(newRange(1,10,4))
print(newRange(20,-5,-3)) 
print(sumOfArray(newRange(1,10)))
print(newRange(1,3))
print(newRange(1,11,2))
print(newRange(1,10,-4))
print(newRange(20,-5,3)) 
