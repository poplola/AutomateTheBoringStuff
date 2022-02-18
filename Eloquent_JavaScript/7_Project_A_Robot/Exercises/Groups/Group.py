class Group:
    def __init__(self):
        self.set = []

    def add(self, x):
        self.set.append(x) if x not in self.set else print(f"Add Data Faild! {x} is already in set {self.set}")
        return self.set

    def delete(self, x):
        self.set.remove(x) if x in self.set else print(f"Delete Data Faild! No data {x} in set {self.set}")
        return self.set

    def has(self, x):
        return x in self.set

mySet = Group()
print(mySet.add(4))
print(mySet.add('4'))
print(mySet.add(14))
print(mySet.add(-5))
print(mySet.add(14))
print(mySet.delete(14))
print(mySet.delete(24))
print(mySet.has(4))
print(mySet.has(24))
print(mySet.has('4'))