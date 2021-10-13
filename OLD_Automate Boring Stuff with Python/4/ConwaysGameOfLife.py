# Conway's Game of life

import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = []             # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Add a live cell
        else:
            column.append('')   # Add a dead cell
    nextCells.append(column)    # nextCells is a list of colunmn list


while True: # Main program loop
    print('\n\n\n\n\n')         # Separate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    # Print currentCellls on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '')         # Print the # or space
        print()  # Print a newline at the end of row


    # Calculate the next step's cells based on current step's cell:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #Count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1   # Top-left neighbor is a live
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1   # Top neighbor is a live
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1   # Top-right neighbor is a live
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1   # Left neighbor is a live
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1   # Right neighbor is a live
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1   # Bottom-left neighbor is a live
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1   # Bottom neighbor is a live     
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1   # Bottom-right neighbor is a live      

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cell with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '' and numNeighbors == 3:
                # Dead cells with 3 neighbors becoe alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ''
        time.sleep(1)   # Add a 1-second pause to reduce flickering
