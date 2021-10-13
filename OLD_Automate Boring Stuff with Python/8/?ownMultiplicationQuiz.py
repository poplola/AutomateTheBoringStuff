import time, random

correctAnswer = 0

for i in range(1, 11):

    num1=random.randint(0,9)
    num2=random.randint(0,9)
    rightAnswer = num1*num2
    # print('num1 = ', num1)
    # print('num2 = ', num2)
    # print('#%s : %s x %s = ')%(str(i), str(num1), str(num2))
    # try:
    startTime = time.time()
    n=1
    overTime = 1
    answer =-1
    while n <= 3:

        # while True:
        try:
            answer = int(input(f'\n#{i} : {num1} x {num2} = '))
            
            if (time.time() - startTime) >= 8:
                print('X - Failed! Passed 8 seconds to answer!')
                overTime = 0
                break
            # print('type of answer: ', type(answer))
            
            if type(answer) == int:
                break
            # if n==3
            
        except:
                print('Please enter an integer number!')
        n+=1

        # print('answer: ', answer)
        
    if (answer == rightAnswer) and overTime and n<=3:
        print('Correct!!!')
        time.sleep(1)
        correctAnswer += 1
        continue
    elif n == 4:
        print('X - Failed! Out of 3 tries!')
    elif answer != rightAnswer:
        print('Wrong answer!')
        # except:
        #     print('Please enter an integer number!')
        #     continue
            
        # break


    # if (time.time() - startTime) > 8:
    #     print('X - Failed! Passed 8 seconds to answer!')
    # if int(answer) != num1*num2:
    #     print('X - Failled! Out of 3 tries!')

print(f'Score : {correctAnswer}/10 correct!')
    
    # print('answer type: ', type(answer))

