"""
FizzBuzz
Write a program that uses console.log to print all the numbers from 1 to 100, with two exceptions. For numbers divisible by 3, print "Fizz" instead of the number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.
When you have that working, modify your program to print "FizzBuzz" for numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz" for numbers divisible by only one of those).
(This is actually an interview question that has been claimed to weed out a significant percentage of programmer candidates. So if you solved it, your labor market value just went up.)
"""

count = 100
for i in range (1, count+1):
    if (not(i%3) and not(i%5)):
        print("FizzBuzz")
    elif not(i%3):
        print("Fizz")
    elif not(i%5):
        print("Buzz")
    else:
        print(i)

