# CPU Scheduling downgraded version to CLI - as MVP
# Thoughts:
# User inputs everything
# User inputs the number of processes and time quantum (for Round Robin)
# User inputs the burst time, arrival time and priority for each process
#------------------------------------------------------------------------------------------------------------
# LIBRARIES

# Function to get the number of processes
# min number of processes = 3
# max number of processes = 10
def get_number_of_processes():
    num_processes = int(input("Enter the number of processes: "))
    if num_processes < 3 or num_processes > 10:
        print("Number of processes must be between 3 and 10")
        num_processes = get_number_of_processes()
    return num_processes

# Function to get the time quantum
def get_time_quantum():
    time_quantum = int(input("Enter the time quantum: "))
    return time_quantum

# Function to get the burst time, arrival time and priority for each process
# format: process name, burst time, arrival time, priority
def get_process_info(num_processes):
    process_info = []
    for i in range(num_processes):
        burst_time = int(input(f"Enter the burst time for P{i}: "))
        arrival_time = int(input(f"Enter the arrival time for P{i}: "))
        priority = int(input(f"Enter the priority for P{i}: "))
        process_info.append((f"P{i}", burst_time, arrival_time, priority))
    print()
    return process_info

def bubble_sort_arrival(process_list):
    """
    Sort the list of processes by their 'arrival' key in ascending order.
    """
    n = len(process_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if process_list[j]['arrival'] > process_list[j + 1]['arrival']:
                process_list[j], process_list[j + 1] = process_list[j + 1], process_list[j]
    return process_list

def bubble_sort_burst(process_list):
    """
    Sort the list of processes by their 'burst' key in ascending order.
    """
    n = len(process_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if process_list[j]['burst'] > process_list[j + 1]['burst']:
                process_list[j], process_list[j + 1] = process_list[j + 1], process_list[j]
    return process_list

def srt_algorithm(process_info):
    """
    Preemptive SRT. Store the extra times in each process dict as well.
    """
    timestamp = 0
    ready_queue = []
    gantt_chart = []

    # Convert each process tuple into a dictionary,
    # storing both the original burst and a modifiable burst field
    processes = []
    for p in process_info:
        processes.append({
            'name': p[0],
            'original_burst': p[1],  # keep original burst for waiting time calculations
            'burst': p[1],          # this will be decremented during execution
            'arrival': p[2],
            'priority': p[3],
            'completion': 0,
            'turnaround': 0,
            'waiting': 0
        })

    bubble_sort_arrival(processes)
    previous_process = None

    # Run until all processes are handled
    while len(processes) or len(ready_queue):
        # Move newly arrived processes to the ready queue
        while processes and processes[0]['arrival'] <= timestamp:
            ready_queue.append(processes.pop(0))

        if ready_queue:
            bubble_sort_burst(ready_queue)        # sort by 'burst' (remaining burst)
            current_process = ready_queue[0]
            if current_process['burst'] == 0:
                # Process is finished
                current_process['completion'] = timestamp
                current_process['turnaround'] = timestamp - current_process['arrival']
                # Use 'original_burst' for correct waiting time
                current_process['waiting'] = current_process['turnaround'] - current_process['original_burst']
                ready_queue.pop(0)
            else:
                # If we just switched processes, record in Gantt chart
                if not previous_process or current_process['name'] != previous_process['name']:
                    gantt_chart.append(current_process)
                current_process['burst'] -= 1  # decrement the remaining burst
                previous_process = current_process
                timestamp += 1
        else:
            # No processes are ready; time advances
            if processes:
                timestamp = processes[0]['arrival']
            else:
                timestamp += 1

    # Update the original process_info with the calculated times
    for process in gantt_chart:
        for p in process_info:
            if p[0] == process['name']:
                p += (process['completion'], process['turnaround'], process['waiting'])

    print("Processes in order after SRT:", [p['name'] for p in gantt_chart])
    print("Original burst times:       ", [p['original_burst'] for p in gantt_chart])
    print("Remaining burst times:      ", [p['burst'] for p in gantt_chart])
    print("Arrival times:              ", [p['arrival'] for p in gantt_chart])
    print("Completion times:           ", [p['completion'] for p in gantt_chart])
    print("Turnaround times:           ", [p['turnaround'] for p in gantt_chart])
    print("Waiting times:              ", [p['waiting'] for p in gantt_chart])
    return gantt_chart

def sjf_algorithm(process_info):
    """
    Non-preemptive SJF that uses dictionaries for each process.
    Stores completion, turnaround, and waiting times in the same dictionary.
    """
    timestamp = 0
    ready_queue = []
    gantt_chart = []

    # Convert each process tuple into a dictionary
    processes = []
    for p in process_info:
        processes.append({
            'name': p[0],
            'burst': p[1],
            'arrival': p[2],
            'priority': p[3],
            'completion': 0,
            'turnaround': 0,
            'waiting': 0
        })

    bubble_sort_arrival(processes)

    while len(processes) != 0 or len(ready_queue) != 0:
        while len(processes) != 0 and processes[0]['arrival'] <= timestamp:
            ready_queue.append(processes.pop(0))

        if len(ready_queue) != 0:
            bubble_sort_burst(ready_queue)
            current_process = ready_queue.pop(0)
            gantt_chart.append(current_process)

            start_time = timestamp
            timestamp += current_process['burst']
            finish_time = timestamp

            current_process['completion'] = finish_time
            current_process['turnaround'] = finish_time - current_process['arrival']
            current_process['waiting'] = current_process['turnaround'] - current_process['burst']
        else:
            timestamp += 1

    # Update the original process_info with the calculated times
    for process in gantt_chart:
        for p in process_info:
            if p[0] == process['name']:
                p += (process['completion'], process['turnaround'], process['waiting'])

    print("Processes in order after SJF:", [p['name'] for p in gantt_chart])
    print("Burst times:                ", [p['burst'] for p in gantt_chart])
    print("Arrival times:              ", [p['arrival'] for p in gantt_chart])
    print("Completion times:           ", [p['completion'] for p in gantt_chart])
    print("Turnaround times:           ", [p['turnaround'] for p in gantt_chart])
    print("Waiting times:              ", [p['waiting'] for p in gantt_chart])
    return gantt_chart

# Test cases for SRT
def test_srt_algorithm_context_switch():
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "4",
            "Enter the burst time for P0: ": "8",
            "Enter the arrival time for P0: ": "0",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "4",
            "Enter the arrival time for P1: ": "1",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "9",
            "Enter the arrival time for P2: ": "2",
            "Enter the priority for P2: ": "3",
            "Enter the burst time for P3: ": "5",
            "Enter the arrival time for P3: ": "3",
            "Enter the priority for P3: ": "4",
        }
        return inputs[prompt]

    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        num_processes = get_number_of_processes()
        process_info = get_process_info(num_processes)
        srt_algorithm(process_info)
    finally:
        __builtins__.input = original_input

test_srt_algorithm_context_switch()

# Test cases for SJF
def test_sjf_algorithm_context_switch():
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "4",
            "Enter the burst time for P0: ": "8",
            "Enter the arrival time for P0: ": "0",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "4",
            "Enter the arrival time for P1: ": "1",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "9",
            "Enter the arrival time for P2: ": "2",
            "Enter the priority for P2: ": "3",
            "Enter the burst time for P3: ": "5",
            "Enter the arrival time for P3: ": "3",
            "Enter the priority for P3: ": "4",
        }
        return inputs[prompt]

    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        num_processes = get_number_of_processes()
        process_info = get_process_info(num_processes)
        sjf_algorithm(process_info)
    finally:
        __builtins__.input = original_input

#------------------------------------------------------------------------------------------------------------
# Main function
def main():
    numProcess = get_number_of_processes()
    timeQuantum = get_time_quantum()
    processInfo = get_process_info(numProcess)

    print("Number of processes: ", numProcess)
    print("Time quantum: ", timeQuantum)
    print("Process info: ", processInfo)


# if __name__ == "__main__":
#     main()
