all: schedSim

schedSim: schedSim.c
        gcc -Wall -Werror -g -o $@ $?

clean:
        -rm -rf schedSim