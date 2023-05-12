"""
Created by Tristan de Lemos and Trenten Spicer
Scheduling Simulator
"""

import sys


def FIFO_printout(size):

    time = 0
    i = 0
    turnaround = 0
    wait = 0
    average_turnaround = 0
    average_wait = 0
    for x in matrix:
        # compute wait time: current time - arrival
        wait = time - x[1]
        if(wait < 0):
            # if there is a gap between previous and next job, go to next job time
            wait = 0
            time = x[1]
        average_wait = average_wait + wait
        # compute current time: run time + original current time
        time = time + x[0]
        # compute turnaround: current time(after job) - arrival
        turnaround = time - x[1]
        average_turnaround = average_turnaround + turnaround
        print(f"Job {i} -- Turnaround {turnaround}  Wait {wait}")
        i += 1

    print(f"Average -- Turnaround {(average_turnaround / size):3.2f}     Wait {(average_wait / size):3.2f}")

def SRTN_printout(size):
    pass
    """""
    time = 0
    index = 0
    turnaround = 0
    wait = 0
    average_turnaround = 0
    average_wait = 0
    # while loop to count each time variable
    while size != 0:
        # check to see if the next job has arrived
        if time == matrix[index][2]:


        # only print a job if it is done
        if (time - matrix[]:
            print(f"Job {i} -- Turnaround {turnaround}  Wait {wait}")
        time += 1

    print(f"Average -- Turnaround {(average_turnaround / size):3.2f}     Wait {(average_wait / size):3.2f}")
"""

def RR_printout(size):
    
    remaining_jobs = size
    time = 0
    job = 0
    while (remaining_jobs != 0):
        q = 3
        while(matrix[job][0] > 0 and q > 0):
            matrix[job][0] -= 1
            time += 1

        if job < size:
            job += 1
        else:
            job = 0

def main():
    """
    """
    SIZE = 0
    # check for valid.txt file
    file = open("test.txt", "r")

    # put what was in.txt file into an array array
    for x in file:
        b = x.split()
        a = [int(b[0]), int(b[1])]
        matrix.append(a)
        SIZE += 1

    print(matrix)
    print(SIZE)

    matrix.sort(key=fifo_key)
    print("fifo:", matrix)

    FIFO_printout(SIZE)

    # sort matrix to base config

    # check for algorithm
    numOfArgs = len(sys.argv)
    if numOfArgs > 1:
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
            FIFO_printout(SIZE)

    else:
        FIFO_printout(SIZE)

    # check for quantum

    # call whichever scheduling algorithm was chosen


def fifo_queue():
    fifo_queue = sorted(matrix, key=fifo_key)
    return fifo_queue

def fifo_key(q):
    return q[1]


if __name__ == "__main__":
    """
    """
    matrix = []
    quantum = 1
    algorithm = "FIFO"
    main()




