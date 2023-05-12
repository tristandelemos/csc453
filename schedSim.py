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



def update_active_jobs(time, active_jobs):
    for job in matrix:
        if (job[1] == time):
            active_jobs.append(job)

def RR_2(size):

    remaining_jobs = size
    avg_wait = 0
    avg_turn = 0
    time = 0
    wait = 0
    turnaround = 0
    job_num = 0

    active_jobs = []
    job_i = 0
    removed_job = False

    update_active_jobs(time, active_jobs)

    while (remaining_jobs > 0):
        removed_job = False
        q = 3
        ran = 0
        if len(active_jobs) < 1:
            time += 1
        else:
            job = active_jobs[job_i]
            while (job[0] > 0 and q > 0):
                if len(job) == 2:
                    job.append(time)
                    job.append(job_num)
                    job_num += 1
                q -= 1
                job[0] -= 1
                time += 1
                update_active_jobs(time, active_jobs)
                ran = 1

            if (job[0] == 0 and ran == 1):
                turnaround = time-job[1]
                wait = job[2]-job[1]
                avg_turn += turnaround
                avg_wait += wait
                print(f"Job {job[3]} -- Turnaround {turnaround}  Wait {wait}")
                remaining_jobs -= 1
                turnaround = 0
                wait = 0
                removed_job = True

            if removed_job:
                pass
            elif job_i == len(active_jobs)-1:
                job_i = 0
            else:
                job_i += 1



def RR_printout(size):
    
    remaining_jobs = size
    avg_wait = 0
    avg_turn = 0
    time = 0
    wait = 0
    turnaround = 0
    job = 0
    while (remaining_jobs != 0):
        q = 3
        ran = 0
        while(matrix[job][0] > 0 and q > 0):
            if len(matrix[job]) == 2:
                matrix[job].append(time)
            # print("job", job)
            matrix[job][0] -= 1
            time += 1
            ran = 1
            q -= 1

        # print(time)
        if (matrix[job][0] == 0) and (ran == 1):
            # print(time, matrix[job][1])
            turnaround = time-1-matrix[job][1]
            # print("turnaround:", turnaround)
            wait = matrix[job][2]-matrix[job][1]
            avg_turn += turnaround
            avg_wait += wait
            print(f"Job {job} -- Turnaround {turnaround}  Wait {wait}")
            remaining_jobs -= 1
            turnaround = 0
            wait = 0

        if job < size-1:
            job += 1
        else:
            job = 0

    avg_wait /= size
    avg_turn /= size
    print(f"Average -- Turnaround {(avg_turn):3.2f}     Wait {(avg_wait):3.2f}")


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

    # FIFO_printout(SIZE)
    # RR_printout(SIZE)
    RR_2(SIZE)

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
        # FIFO_printout(SIZE)
        pass

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




