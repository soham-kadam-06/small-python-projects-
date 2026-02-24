# FCFS Scheduling with Arrival Time

process = int(input("Enter number of processes: "))

Arr = []  # Arrival time
Bru = []  # Burst time

for i in range(process):
    Arr.append(int(input(f"Enter Arrival Time for P{i+1}: ")))
    Bru.append(int(input(f"Enter Burst Time for P{i+1}: ")))

start = [0] * process
finish = [0] * process
tat = [0] * process
wt = [0] * process

for i in range(process):
    if i == 0:
        start[i] = Arr[i]
    else:
        # Start time is either when CPU becomes free or process arrives (whichever is later)
        start[i] = max(Arr[i], finish[i-1])
    
    # Finish time = start + burst
    finish[i] = start[i] + Bru[i]

    # Turnaround time = finish - arrival
    tat[i] = finish[i] - Arr[i]

    # Waiting time = turnaround - burst
    wt[i] = tat[i] - Bru[i]

# Display results
print("\nProcess\tArrival\tBurst\tStart\tFinish\tWaiting\tTurnaround")
for i in range(process):
    print(f"P{i+1}\t{Arr[i]}\t{Bru[i]}\t{start[i]}\t{finish[i]}\t{wt[i]}\t{tat[i]}")

print(f"\nAverage Waiting Time: {sum(wt)/process:.2f}")
print(f"Average Turnaround Time: {sum(tat)/process:.2f}")

# gantt chart 
print("gantt chart")
for i in range(process):
    print(f"|  p{i+1}", end="")
print("|")
for i in range(process):
    print(start[i], end="\t")
print(finish[-1])