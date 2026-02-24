# Memory Allocation Algorithms: First Fit, Best Fit, Worst Fit

def first_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
    return allocation


def best_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        best_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if best_index == -1 or block_size[j] < block_size[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[i]
    return allocation


def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        worst_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if worst_index == -1 or block_size[j] > block_size[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_size[worst_index] -= process_size[i]
    return allocation


# ---------------- MAIN PROGRAM ----------------
# User input for memory blocks
n = int(input("Enter number of memory blocks: "))
block_size = []
for i in range(n):
    size = int(input(f"Enter size of block {i+1}: "))
    block_size.append(size)

# User input for processes
m = int(input("\nEnter number of processes: "))
process_size = []
for i in range(m):
    size = int(input(f"Enter size of process {i+1}: "))
    process_size.append(size)

# Display input
print("\nMemory Blocks:", block_size)
print("Processes:", process_size)

# -------- FIRST FIT --------
print("\n--- First Fit ---")
alloc1 = first_fit(block_size.copy(), process_size)
for i in range(len(process_size)):
    if alloc1[i] != -1:
        print(f"Process {i+1} ({process_size[i]}) → Block {alloc1[i]+1}")
    else:
        print(f"Process {i+1} ({process_size[i]}) → Not Allocated")

# -------- BEST FIT --------
print("\n--- Best Fit ---")
alloc2 = best_fit(block_size.copy(), process_size)
for i in range(len(process_size)):
    if alloc2[i] != -1:
        print(f"Process {i+1} ({process_size[i]}) → Block {alloc2[i]+1}")
    else:
        print(f"Process {i+1} ({process_size[i]}) → Not Allocated")

# -------- WORST FIT --------
print("\n--- Worst Fit ---")
alloc3 = worst_fit(block_size.copy(), process_size)
for i in range(len(process_size)):
    if alloc3[i] != -1:
        print(f"Process {i+1} ({process_size[i]}) → Block {alloc3[i]+1}")
    else:
        print(f"Process {i+1} ({process_size[i]}) → Not Allocated")
