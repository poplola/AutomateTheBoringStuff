import pyperclip, pathlib, os, glob, re

for i in range(1, 4):
    testF = open(f'testF_{i}.txt', 'w')
    testF.write('')
    for j in range(1, 6):
        testF = open(f'testF_{i}.txt', 'a')
        testF.write(f' {i} X {j} = {i*j}\n')
        testF.close()

filePath = '/Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/9/regexSearch/'
myFiles = glob.glob('*.txt')
print(myFiles)


rowStr = r'= 1'

fRegex = re.compile(rowStr)

for i in range(1, len(myFiles)+1):
    f = open(f'testF_{i}.txt', 'r')
    # print(f'file {i} : ', f.read())
    text = f.read()
    print(f'text {i} : \n', text)
    mo = fRegex.findall(text)
    print(f"\nfile {i} found '{rowStr}' : %s\n"%(len(mo)))
    print(mo)
    