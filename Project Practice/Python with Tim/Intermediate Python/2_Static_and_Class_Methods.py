#2 Static and Class Methods
# for orgnising the class methods in code


# <===== Practice 1:   =====>
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
        classmethod is you can call any instance/variables inside of the class, 
        you do not need to create any object to use the methods that marked as classmethod decorator
        also, no need 'self' as parameter, at lease one parameter to pass the class object
        eg: call directly ==> person.getPopulation()
    """
    @classmethod    
    def getPopulation(cls):     # at lease one paramenter 'cls' here
        return cls.population

    """
        staticmethod is that you can not use or access the variables inside of class, 
        only through passed parmeters
        you do not need to create any object to use the methods that marked as staticmethod decorator
        also, don't take 'self' or class as parameter, no parameter still works fine
        eg: call directly ==> person.isAdult(2)
    """
    @staticmethod
    def isAdult(age):   # no need parameter 'age' here, just for compare
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = person('lisa', 41)

# use classmethod directly
print(person.getPopulation())

print(person.isAdult(21))




# <===== Practice 2:  =====>


# <===== Practice 3:  =====>
