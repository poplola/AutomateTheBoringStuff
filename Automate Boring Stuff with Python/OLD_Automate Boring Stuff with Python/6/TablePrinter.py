
print('\n=====================================================================\n')

# Print list of list
def printTable(tableList, rNum):
    
    for numList in tableList:
        numColum = len(numList)

    for y in range(numColum):
        for x in range(len(tableList)):
            print(tableList[x][y].rjust(rNum), end = ' ')
        print()


def main():

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

    numLongest = 0
    
    # Check the longest number of word characters
    for xRow in tableData:
        for yColum in xRow:
            if len(yColum) > numLongest:
                numLongest = len(yColum) 
   
    printTable(tableData, numLongest)


if __name__ == "__main__": main()

print('\n=====================================================================\n')
