import pyinputplus as pyip
import random, time


print('\n'+'='*100+'\n')

numberOfQuestions = 10
correctAnswer = 0

for questionNumber in range(numberOfQuestions):
    # Pick 2 random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s * %s = '%(questionNumber,num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)],
                      blockRegexes=['.*', 'Incorrect!'],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of 8 seconds time!')
    except pyip.RetryLimitException:
        print('Out of 3 tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct answer!')
        correctAnswer += 1
    print()
    time.sleep(1)

print('\nYou got %s/%s questions correct!\n'%(correctAnswer,numberOfQuestions))



print('\n'+'='*100+'\n')