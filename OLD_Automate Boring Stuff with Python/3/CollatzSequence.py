
def collatz(number):
    if number % 2 == 0:
       print(number // 2, f' : {number} // 2')
       return number // 2
    else:
        print(3 * number + 1, f' : 3 * {number} + 1')
        return 3 * number + 1



def main():
    print('Enter a number:')

    
    while True:
        try:
            n = int(input())
        except ValueError:
            print('Please enter an integer number: ')
            continue
        break

    while True:
        n = collatz(n)
        if n == 1:
            break



if __name__ == "__main__": main()
