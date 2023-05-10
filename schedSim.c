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
int ** matrix;
int quantum = 1;
FILE * file_pointer;

int SIZE;               // how many jobs we have

// function to print out FIFO algorithm
int FIFO_print_out(){
    // start with testing how the file will appear

    int i;
    int arrival = 0;

    for (i = 0; i < SIZE; i++){
        // find next highest arrival time
        
    }
    


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

int put_into_array(){
    char * line = malloc(sizeof(char) * 2);
    int i = 0;
    while(getline(line, sizeof(char) * 2, file_pointer) != -1){
        matrix[i][0] = i;
        matrix[i][1] = line[0];
        matrix[i][2] = line[1]; 
    }
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
