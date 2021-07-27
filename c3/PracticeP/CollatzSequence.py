

def collatz(number):
    if number % 2:
        number = 3 * number + 1
    else:
        number = number // 2
    
    return number

while True:
    try:
        num = int(input("Enter number : "))
    except ValueError:
        print("Please input an integer number!")
        continue
    break

while True:
    if num == 1:
        break
    num = collatz(num)
    print(num)

