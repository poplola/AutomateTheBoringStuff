#6 Context Managers
"""
'with' keyword is to start a context manager

Practice 1: return a function inside of a function 
Practice 2: 'with open() as ..' to start context manager to open and close files, etc
Practice 3: write context manager class and how to handle exception
Practice 4: decorator / generator used in context manager
"""


# <===== Practice 1: return a function inside of a function =====>
print("\n<===== Practice 1: return a function inside of a function =====>\n")
import os
from pathlib import Path
os.chdir(f"{Path.cwd()}/Python with Tim/Expert Python/")

file = open('file.txt', 'w')
try:
    file.write('Practice 1! ')
finally:
    file.close()



# <===== Practice 2: 'with open() as ..' to start context manager to open and close files, etc =====>
print("\n<===== Practice 2: 'with open() as ..' to start context manager to open and close files, etc =====>\n")
with open('file.txt', 'a') as file:
    file.write('Practice 2! ')



# <===== Practice 3: write context manager class and how to handle exception =====>
print("\n<===== Practice 3: write context manager class and how to handle exception =====>\n")
class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):    # '__enter__': the first method to run in the code
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):     # type, value, traceback: to get exception info
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        # how to handle the certain type exception
        if type == Exception:
            return True     # if decide the exception is accept, return True not to crash code

with File("file.txt", "a") as f:
    print("Middle")
    f.write("Practice 3! ")
    raise Exception   # Exception is handled, not crash code
    # raise FileExistsError   # FileExistsError is not handled, code crashed


# <===== Practice 4: decorator / generator used in context manager =====>
print("\n<===== Practice 4: decorator / generator used in context manager =====>\n")
from contextlib import contextmanager

@contextmanager     # decorator
def file(filename, method):
    print("Enter")
    file = open(filename, method)
    yield file      # generator
    file.close()
    print("Exit")

with file("text.txt", "a") as f:
    print("middle")
    f.write("Practice 4! ")


print()