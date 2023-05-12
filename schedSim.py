"""
Created by Tristan de Lemos and Trenten Spicer
Scheduling Simulator
"""

import sys

def main():
    """
    """
    matrix = []
    # check for valid.txt file
    file = open("test.txt", "r")
    SIZE = 0

    # put what was in.txt file into an array array
    for x in file:
        a = []
        a.append(x[0])
        a.append(x[2])
        matrix.append(a)
        SIZE += 1

    print(matrix)
    print(SIZE)

    # sort matrix to base config

    # check for algorithm
    numOfArgs = len(sys.argv)
    if numOfArgs == 5:
        #round robin
        pass
    

    # check for quantum

    # call whichever scheduling algorithm was chosen





if __name__ == "__main__":
    """
    """
    main()




