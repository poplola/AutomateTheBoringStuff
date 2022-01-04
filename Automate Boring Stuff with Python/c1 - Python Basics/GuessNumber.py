import random

num = random.randint(1, 20)
count = 1
print("I am thinking of a number between 1 and 20")

while True:

    print(f"\nTake a guess {count}: ")

    guess = int(input())

    if guess == num:
        print(f"Good Job! You guessed my number in {count} guess(es)!")
        break
    elif guess > num:
        print("Your guess is too high.")
    else:
        print("Your guess is too low!")
    
    count += 1

