#!user/bin/env python3
"""
Created by Tristan de Lemos and Trenten Spicer
Scheduling Simulator
"""

import sys


def FIFO_printout(size):
    #iterate through basic queue

    time = 0
    i = 0
    turnaround = 0
    wait = 0
    average_turnaround = 0
    average_wait = 0
    for x in matrix:
        print(x)
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
    remaining_jobs = size
    avg_wait = 0
    avg_turn = 0
    time = 0
    wait = 0
    turnaround = 0
    job_num = 0

    active_jobs = []
    

    while remaining_jobs > 0:
        # update queue and sort
        update_active_jobs(time, active_jobs)
        for job in active_jobs:
            if len(job) == 2:
                job.append(job_num)
                job_num += 1
        active_jobs.sort(key=srtn_key)
        # print(active_jobs)

        

        if len(active_jobs) == 0:
            time += 1
        else:
            # better name
            job = active_jobs[0]
            # initial appends
            if len(job) == 3:
                job.append(time)
                job.append(0)

            #decrement job
            job[0] -= 1
            #increase time
            time += 1
            
            #add post-start wait time for other processese
            for x in active_jobs:
                if len(x) == 5:
                    x[4] += 1
            
            #remove wait time from this process
            job[4] -= 1

            #if job complete
            if(job[0] == 0):
                #turnaround = end time - arrival time
                turnaround = time-job[1]
                #wait = start time - arrival time + wait time
                wait = (job[3]-job[1]) + job[4]
                #contribute to avg
                avg_turn += turnaround
                avg_wait += wait
                #output
                print(f"Job {job[2]} -- Turnaround {turnaround}  Wait {wait}")
                #decrement jobs
                remaining_jobs -= 1
                # reset local vars
                turnaround = 0
                wait = 0
                #remove from active queue
                active_jobs.pop(0)
    #avg print
    print(f"Average -- Turnaround {(avg_turn / size):3.2f}     Wait {(avg_wait / size):3.2f}")



def update_active_jobs(time, active_jobs):
    #update jobs in active queue
    for job in matrix:
        if (job[1] == time):
            active_jobs.append(job.copy())


def RR_3(size, quantum):

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

    tiebreaker = False

    n = 0

    #initial jobs
    update_active_jobs(time, active_jobs)

    while (remaining_jobs > 0):
        n+=1
        # print(active_jobs)
        # print("time:", time)
        removed_job = False
        q = quantum
        ran = 0
        #allocate for gaps
        if len(active_jobs) < 1:
            time += 1
            update_active_jobs(time, active_jobs)
        else:
            # print(job_i)
            #better name
            job = active_jobs[0]
            # print("current job:", job)
            #go through quantum, ends early if job finishes
            while (job[0] > 0 and q > 0):
                #inits
                if len(job) == 2:
                    job.append(time)
                    job.append(job_num)
                    job.append(0)
                    job_num += 1
                #decrement
                job[0] -= 1
                q -= 1
                #increment time
                time += 1
                
                #add waits
                for x in active_jobs:
                    if len(x) == 5:
                        x[4] += 1
                
                #remove wrong wait for this process
                if job[0] != 0:
                    job[4] -= 1
                
                #determine tiebreaker (whether job needs to be returned to queue before new jobs)
                if q == 0 and job[0] > 0:
                    tiebreaker = True
                else:
                    # print("not tiebreaker")
                    update_active_jobs(time, active_jobs)

            if job[0] == 0:
                #turnaround = end time - arrival time
                turnaround = time-job[1]
                #wait = wait + start - arrival
                wait = job[4] + job[2] - 1 - job[1]
                avg_turn += turnaround
                avg_wait += wait
                print(f"Job {job[3]} -- Turnaround {turnaround}  Wait {wait}")
                remaining_jobs -= 1
                # print("remaining:", remaining_jobs, "time:", time)
                turnaround = 0
                wait = 0
                #remove from active queue
                active_jobs.pop(0)
                # print(active_jobs)
                removed_job = True
            #if tiebreaker, append old job first
            elif tiebreaker:
                active_jobs.append(job.copy())
                active_jobs.pop(0)
                update_active_jobs(time, active_jobs)
                tiebreaker = False
            else:
                active_jobs.append(job.copy())
                active_jobs.pop(0)
                

        # # break
        # if n > 40:
        #     break

    avg_wait /= size
    avg_turn /= size
    print(f"Average -- Turnaround {(avg_turn):3.2f}     Wait {(avg_wait):3.2f}")

    


def main():
    """
    """
    SIZE = 0
    algorithm = "FIFO"
    quantum = 1
    # check for valid.txt file
    # file = open("test.txt", "r")

    # put what was in.txt file into an array array
    

    # print(matrix)
    # print(SIZE)

    # print("fifo:", matrix)

    # FIFO_printout(SIZE)
    # RR_printout(SIZE)
    # RR_2(SIZE)
    # SRTN_printout(SIZE)

    # sort matrix to base config

    # check for algorithm
    numOfArgs = len(sys.argv)
    if numOfArgs > 1:
        file = open(str(sys.argv[1]), "r")
    else:
        file = open("test.txt", "r")

    for x in file:
        b = x.split()
        a = [int(b[0]), int(b[1])]
        matrix.append(a)
        SIZE += 1

    matrix.sort(key=fifo_key)

    if "-p" in sys.argv:
        algorithm = sys.argv[sys.argv.index("-p")+1]
    if "-q" in sys.argv:
        quantum = sys.argv[sys.argv.index("-q")+1]
        

    if numOfArgs == 3 or numOfArgs == 5 or numOfArgs > 6:
        print("Usage: schedSim <job-file.txt> -p <ALGORITHM> -q <QUANTUM>")
        return 0


    # print(algorithm)
    # print(quantum)

    if algorithm == "SRTN":
        SRTN_printout(SIZE)
    elif algorithm == "RR":
        RR_3(SIZE, (int)(quantum))
    else:
        FIFO_printout(SIZE)


    # check for quantum

    # call whichever scheduling algorithm was chosen


def fifo_queue():
    fifo_queue = sorted(matrix, key=fifo_key)
    return fifo_queue

def fifo_key(q):
    return q[1]

def srtn_key(q):
    return q[0]


if __name__ == "__main__":
    """
    """
    matrix = []
    quantum = 1
    algorithm = "FIFO"
    main()




