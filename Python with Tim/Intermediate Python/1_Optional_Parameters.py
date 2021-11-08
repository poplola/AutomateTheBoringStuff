#1 Optional Parameters


# # <===== Practice 1:  call function without parameters =====>
# def func(x=2):  # x default value is 2
#     return x **2

# call = func(5)
# # call = func()
# print(call)


# # <===== Practice 2: frequancy print =====>
# def func(word, freq=1, add=5):
#     print(word*(freq + add))

# call = func('lisa', 10, 15)


# <===== Practice 3: given default value of parmeter in Car class to make easier code =====>
class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):  # do not need to pass condition/kms value as a new car
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):    # showAll default is True unless pass parameter is false
        if showAll:
            print(f"This car is a {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.kms} kms.")
        else:
            print(f"This car is a {self.make} {self.model} from {self.year}")

whip = car('Ford', 'Fusion', 2012)
whip.display()          
whip.display(False)