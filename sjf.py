n = int(input("Enter number of processes: "))
process = []

# Input arrival and burst times
for i in range(n):
    Arr = int(input(f"Enter Arrival time for P{i+1}: "))
    Bru = int(input(f"Enter Burst time for P{i+1}: "))
    process.append({'id': i+1, 'Arr': Arr, 'Bru': Bru})

# Sort processes by Burst Time
process.sort(key=lambda x: x['Bru'])

# Initialize
Start = [0] * n
Finish = [0] * n
Waiting = [0] * n
TAT = [0] * n

# Calculate start, finish, waiting, and turnaround times
for i in range(n):
    if i == 0:
        Start[i] = process[i]['Arr']
    else:
        Start[i] = max(Finish[i-1], process[i]['Arr'])
    Finish[i] = Start[i] + process[i]['Bru']
    TAT[i] = Finish[i] - process[i]['Arr']
    Waiting[i] = TAT[i] - process[i]['Bru']

# Print results
print("\nProcess\tAT\tBT\tWT\tTAT")
for i in range(n):
    p = process[i]
    print(f"P{p['id']}\t{p['Arr']}\t{p['Bru']}\t{Waiting[i]}\t{TAT[i]}")

print("\nAverage Waiting Time:", sum(Waiting)/n)
print("Average Turnaround Time:", sum(TAT)/n)

# Gantt Chart
print("\nGantt Chart:")
for i in range(n):
    print(f"|  P{process[i]['id']}  ", end="")
print("|")
for i in range(n):
    print(f"{Start[i]:<5}", end="")
print(Finish[-1])
