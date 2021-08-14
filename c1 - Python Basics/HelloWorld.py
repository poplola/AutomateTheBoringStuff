message = 'Hello World!'
print(message + '\nWhat is your name?')
name = input()
print("It's goog to meet you, " + name)
print("The length of your name is: ", len(name))
print("What is your age?")
age = round(float(input()))
print(f"Hi {name}, you will be {age+1} next year.")