"""
Program: Conway's Game of Life
"""

import random
import time
import copy
WIDTH = 60
HEIGH = 20

# Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGH):
        if random.randint(0, 1):
            column.append("#")  # Add a living cell
        else:
            column.append(" ")  # Add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

while True:  # Main program loop
    print("\n\n\n\n\n")  # Add newlines after each run
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the scrreen
    for y in range(HEIGH):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # Print the # or space
        print()  # Print newline at the end of each row

    # Calculate the next step's cells based on current step's cells
    for y in range(HEIGH):
        for x in range(WIDTH):
            #  Get neighboring coordinates
            # '% WIDTH' ensure leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGH
            belowCoord = (y + 1) % HEIGH

            # Count the number of living neighbors
            numNeighnor = 0
            if currentCells[leftCoord][aboveCoord] == "#":  # Top-left neighbor is alive
                numNeighnor += 1
            if currentCells[leftCoord][belowCoord] == "#":  # Bottom-left neighbor is alive
                numNeighnor += 1
            if currentCells[leftCoord][y] == "#":  # Left neighbor is alive
                numNeighnor += 1
            if currentCells[rightCoord][aboveCoord] == "#":  # Top-right neighbor is alive
                numNeighnor += 1
            # Bottom-right neighbor is alive
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighnor += 1
            if currentCells[rightCoord][y] == "#":  # Right neighbor is alive
                numNeighnor += 1
            if currentCells[x][aboveCoord] == "#":  # Top neighbor is alive
                numNeighnor += 1
            if currentCells[x][belowCoord] == "#":  # Bottom neighbor is alive
                numNeighnor += 1

            # Set cells based on Game of Life rules
            if currentCells[x][y] == "#" and (numNeighnor == 2 or numNeighnor == 3):
                # Living cell with 2 or 3 neighbors stay alive
                nextCells[x][y] = "#"
            elif currentCells[x][y] == ' ' and numNeighnor == 3:
                # Dead cell with 3 neighbor become alive
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stay dead
                nextCells[x][y] = " "
    time.sleep(1) # Add 1 second pause to reduce flickering.