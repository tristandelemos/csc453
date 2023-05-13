Tristan de Lemos and Trenten Spicer

When running the program on Unix servers, you have to write "python3 ./schedSim.py ....." It look a long time for us to figure this out.

For what types of workloads does SRTN deliver the same turnaround times as FIFO?
If all of the jobs have the same run times, then these algorithms deliver the same turnaround time.

For what types of workloads and quantum lengths does SRTN deliver the same response times as RR?
If all the jobs have the same run time and the runtime and quantum are the same value.

What happens to response time with SRTN as job lengths increase? Can you use the simulator to demonstrate the trend?
The response time will decline because SRTN always favors the smallest job, which will make the longer jobs take even longer to complete. To simulate this, we would have longer jobs be added at every interval of 5. This would make all of the jobs have a much longer response time.

What happens to response time with RR as quantum lengths increase? Can you write an equation that gives the worst-case response time, given N jobs?
As quantum lengths increase, the response time will decrease which will lower the efficiency. The worst case scenario is when 
