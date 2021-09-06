# directory = '/Users/Programs/Directory/program1.csv'
# endIndex = directory.rfind(".")
# startIndex = directory.rfind("/")
# print(directory[startIndex+1:endIndex])
# print(startIndex, endIndex)

# directory = '/Users/Programs/Directory/program1.csv'
# print(directory.rpartition('.')[0].split('/')[-1])
# print(directory.rpartition('.'))

# import pathlib
 
# directory = '/Users/Programs/Directory/program1.csv'
# filename = pathlib.Path(directory).stem
 
# print(filename)

l = [2,4,5,3,3,2,4,5,6,7,3,2]
d = set(l)
# d = set((i, l.count(i)) for i in l if l.count(i)>1)
# print(set((i, l.count(i)) for i in l if l.count(i)>1))

print(d)
# for item in d:
#     print(f"Vaule <{item[0]}> appeared {item[1]} times.")