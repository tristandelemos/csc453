/*
Created by Tristan de Lemos and Trenten Spicer
On May 8th 2023
Lab 2 CSC 453
Given a text file and algorithm to run, 
this simulator will show how that algorithm will run with jobs in the .txt file

*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_SIZE 1024

char * algorithm;       // scheduling algorithm to use
int ** matrix;          // data structure to hold tuple
int ** fifo_matrix;     // data structure to hold sorted tuple
int quantum = 1;        // base quantum for Round Robin
FILE * file_pointer;    // file pointer for file

int SIZE;               // how many jobs we have

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

// function to print out FIFO algorithm
int FIFO_print_out(){
    // start with testing how the file will appear

    int time = 0;
    int i;
    int turnaround;
    int wait;
    int average_turnaround = 0;
    int average_wait = 0;
    for (i = 0; i < SIZE; i++){
        // compute wait time: current time - arrival 
        wait = time - matrix[i][1];
        average_wait = average_wait + wait;
        // compute current time: run time + original current time
        time = time + matrix[i][0];
        // compute turnaround: current time(after job) - arrival
        turnaround = time - matrix[i][1];
        average_turnaround = average_turnaround + turnaround;
        
        printf("Job %3d -- Turnaround %3.2f     Wait %3.2f", i, turnaround, wait);
    }
    
    printf("Average -- Turnaround %3.2f     Wait %3.2f", (average_turnaround/SIZE), (average_wait/SIZE));


    return 0;
}

// function to print out SRTN algorithm
int SRTN_print_out(){



    return 0;
}

// function to print out RR algorithm
int RR_print_out(){



    return 0;
}

int sort_arrival_times() {

    int added = 0;
    int arrival_time = 0;
    int i = 0;
    while (added < SIZE) {
        //rollover for matrix
        if (i == SIZE) {
            i = 0;
            arrival_time ++;
        }
        //check if job is at current arrival time
        if (matrix[i][1] == arrival_time) {
            //add job to sorted matrix
            fifo_matrix[added] = matrix[i];
            added ++;
        }
        //increment i to look at next job
        i++;

    }
    printf("sorted\n");
    return 0;

}


int put_into_array(){
    char * line = malloc(sizeof(char) * 2);
    int i = 0;
    // read everything from the file into the matrix
    while(getline(&line, (size_t) (sizeof(char) * 2), file_pointer) != -1){
        matrix[i][0] = line[0];
        matrix[i][1] = line[1]; 
        i++;
    }
    SIZE = i;

    // sort
    qsort(matrix, SIZE, sizeof(int) * 2, cmpfunc);

    for (i = 0; i < SIZE; i++)
    {
        printf("run: %d, arrive: %d\n", matrix[i][0], matrix[i][1]);
    }
    return 0;
}


int main(int argc, char const *argv[]){

    // check for valid .txt file
    if((file_pointer = fopen(argv[1], "r")) < 0){
        printf("Text file is not valid. End program.\n");
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    // malloc area for each entry in memory
    matrix = malloc(sizeof(int) * MAX_SIZE);
    int i;
    for (i = 0; i < MAX_SIZE; i++){
        matrix[i] = malloc(sizeof(int) * 2);
    }
    
    // put what was in .txt file into an array array
    put_into_array();
    fclose(file_pointer);

    //sort matrix to base config
    fifo_matrix = malloc(sizeof(int) * SIZE);
    for (i=0; i<SIZE; i++) {
        fifo_matrix[i] = malloc(sizeof(int) * 2);
    }
    sort_arrival_times();


    // check for algorithm
    if(argc < 2){
        // algorithm not given, use FIFO
        algorithm = "FIFO";
    }
    else{
        // not write
        strcpy(algorithm, argv[2]);
    }

    // check for quantum
    if(argc > 5){
        // check where q is
    }

    // call whichever scheduling algorithm was chosen
    if(strcmp(algorithm, "SRTN") == 0){
        SRTN_print_out();
    }
    else if (strcmp(algorithm, "RR") ==  0){
        RR_print_out();
    }
    else{
        FIFO_print_out();
    }
    
    

    // free up all memory used
    for (i = 0; i < MAX_SIZE; i++){
        free(matrix[i]);
    }

    return 0;
}
