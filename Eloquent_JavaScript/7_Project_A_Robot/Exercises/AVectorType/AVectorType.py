class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, vecX, vecY):
        return f"Sum of two vectors ({self.x}, {self.y}) and ({vecX}, {vecY}) ==> ({self.x + vecX}, {self.y + vecY})"

    def minus(self, vecX, vecY):
        return f"Difference of two vectors ({self.x}, {self.y}) and ({vecX}, {vecY}) ==> ({self.x - vecX}, {self.y - vecY})"
    
    def __get__(self):
        return f"The distance of the point ({self.x}, {self.y}) from the origin (0, 0) ==> ({abs(self.x)}, {abs(self.y)}) "

vec1 = Vec(-4, -8)
print(vec1.plus(2,5))
print(vec1.minus(9,3))
print(vec1.__get__())
