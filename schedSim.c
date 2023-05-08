/*
Created by Tristan de Lemos and Trenten Spicer
On May 8th 2023
Lab 2 CSC 453
Given a text file and algorithm to run, 
this simulator will show how that algorithm will run with jobs in the .txt file

*/

#include <stdlib.h>
#include <stdio.h>
#define MAX_SIZE 1024

char * algorithm;       // scheduling algorithm to use
int ** matrix;

int SIZE;               // how many jobs we have

int FIFO_print_out(){
    // start with testing how the file will appear

    int i;
    int arrival = 0;

    for (i = 0; i < SIZE; i++){
        // find next highest arrival time
        
    }
    


    return 0;
}




int main(int argc, char const *argv[]){

    // check for valid .txt file


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
        algorithm = argv[2];
    }

    // free up all memory used
    for (i = 0; i < MAX_SIZE; i++){
        free(matrix[i]);
    }

    return 0;
}
