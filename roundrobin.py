def round_robin():
    n = int(input("Enter the number of processes: "))

    process = []
    for i in range(n):
        at = int(input(f"Enter Arrival time for p{i+1}: "))
        bt = int(input(f"Enter Burst time for p{i+1}: "))
        process.append([f"p{i+1}", at, bt])

    qt = int(input("Enter the quantum number: "))

    process.sort(key=lambda x: x[1])
    bt_remaining = [p[2] for p in process]
    time = 0
    completed = 0
    gantt_process = []
    gantt_times = []
    result_table = []
    total_tat = 0
    total_wt = 0
    finish_time = [0] * n
    ready_queue = []

    # Round-robin scheduling using indices into process list
    while completed < n:
        # enqueue arrived processes that are not already in ready_queue and not finished
        for idx, p in enumerate(process):
            if p[1] <= time and idx not in ready_queue and bt_remaining[idx] > 0:
                ready_queue.append(idx)

        if not ready_queue:
            time += 1
            continue

        idx = ready_queue.pop(0)
        exec_time = min(qt, bt_remaining[idx])
        bt_remaining[idx] -= exec_time
        gantt_process.append(process[idx][0])
        gantt_times.append(time)
        time += exec_time

        # add any newly arrived processes during execution
        for jdx, p in enumerate(process):
            if p[1] <= time and jdx not in ready_queue and bt_remaining[jdx] > 0 and jdx != idx:
                ready_queue.append(jdx)

        if bt_remaining[idx] == 0:
            completed += 1
            finish_time[idx] = time
            total_tat += finish_time[idx] - process[idx][1]
            total_wt += (finish_time[idx] - process[idx][1] - process[idx][2])
        else:
            ready_queue.append(idx)

    gantt_times.append(time)

    print("\nGantt Chart:")
    for i in range(len(gantt_process)):
        print(f"{gantt_process[i]} | {gantt_times[i]} -> {gantt_times[i+1]}")

    print("\nResults:")
    print("PID\tAT\tBT\tFT\tTAT\tWT")
    for idx, p in enumerate(process):
        ft = finish_time[idx]
        tat = ft - p[1]
        wt = tat - p[2]
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{ft}\t{tat}\t{wt}")

    print(f"\nAverage TAT: {total_tat / n:.2f}")
    print(f"Average WT: {total_wt / n:.2f}")


if __name__ == "__main__":
    round_robin()

