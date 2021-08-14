#! Python3
# Write Your Own Multiplication Quiz
"""
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

    1. If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
    2. The user gets three tries to enter the correct answer before the program moves on to the next question.
    3. Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.

Compare your code to the code using PyInputPlus in “Project: Multiplication Quiz” on page 196.
"""

import random, time

print('\n'*2) 
print("="*70)
print("     Multiplication Quiz     ".center(70, '='))
print("=" * 70 + '\n')

numberOfQuiz = 5
waitTime = 5
answerTries = 3
correctCount = 0

for i in range(numberOfQuiz):
    x = random.randint(0, 9)
    y = random.randint(0, 9)

    for j in range(answerTries):

        while True:

            try:       
                currentTime = time.time()            
                print(f"#{i+1} : {x} X {y} = ", end='')   
                answer = int(input())
            except ValueError:
                print("Please input a int number!\n")
                continue
            else:
                break

        if time.time() - currentTime > waitTime:
            print(f"Failed! Answer over {waitTime} seconds. ")
            break

        if answer != x * y:
            if j+1  == answerTries :
                print(f"Faild! You have got {answerTries} tries with worng answers!")
                break            
            print("Wong Answer!\n")
            print(f"({j+2} of {answerTries} tries )\n", end='')
            continue
        else:
            print("Correct!!!")
            time.sleep(1)
            correctCount += 1
            break

        

    print('\n')
    
print(f"    Score : {correctCount} / {numberOfQuiz} correct!    ".center(70,'='))           
print('\n'*2)


