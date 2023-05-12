"""
Created by Tristan de Lemos and Trenten Spicer
Scheduling Simulator
"""

import sys


def FIFO_printout():

    time = 0
    i = 0
    turnaround = 0
    wait = 0
    average_turnaround = 0
    average_wait = 0
    for x in matrix:
        # compute wait time: current time - arrival
        wait = time - x[1]
        average_wait = average_wait + wait
        # compute current time: run time + original current time
        time = time + x[0]
        # compute turnaround: current time(after job) - arrival
        turnaround = time - x[1]
        average_turnaround = average_turnaround + turnaround
        print(f"Job {i} -- Turnaround {turnaround}  Wait {wait}")
        i += 1

    print(f"Average -- Turnaround {(average_turnaround / SIZE)}     Wait {(average_wait / SIZE)}")



def SRTN_printout():
    pass

def RR_printout():
    pass


def main():
    """
    """
    # check for valid.txt file
    file = open("test.txt", "r")
    SIZE = 0

    # put what was in.txt file into an array array
    for x in file:
        a = [x[0], x[2]]
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
    if sys.argv[2] == "q":
        quantum = sys.argv[3]
    if sys.argv[2] == "p":
        algorithm = sys.argv[3]

    if sys.argv[4] == "q":
        quantum = sys.argv[5]

    if algorithm == "SRTN":
        SRTN_printout()
    elif algorithm == "RR" or numOfArgs >3:
        RR_printout()
    else:
        FIFO_printout()


    # check for quantum

    # call whichever scheduling algorithm was chosen





if __name__ == "__main__":
    """
    """
    matrix = []
    quantum = 1
    algorithm = "FIFO"
    SIZE = 0
    main()




