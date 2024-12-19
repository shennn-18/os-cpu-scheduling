#CPU Scheduling downgraded version to CLI - as MVP
#Thoughts:
# User inputs everything
# User inputs the number of processes and time quantum (for Round Robin)
# User inputs the burst time, arrival time and priority for each process
#------------------------------------------------------------------------------------------------------------
# LIBRARIES
# import customtkinter as ctk
# import tkinter as tk
# from tkinter import ttk

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

#------------------------------------------------------------------------------------------------------------
# CPU Scheduling Algorithms & Related Functions

# swap function
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b

# Bubble sort burst time
def bubble_sort_burst(tup_list):
    n = len(tup_list)
    for i in range(n - 1):
        for j in range (n - i - 1):
            if tup_list[j][1] > tup_list[j+1][1]:
                tup_list[j], tup_list[j + 1] = swap (tup_list[j], tup_list[j + 1])
    return tup_list

# Bubble sort arrival time
def bubble_sort_arrival(tup_list):
    n = len(tup_list)
    for i in range(n - 1):
        for j in range (n - i - 1):
            if tup_list[j][2] > tup_list[j+1][2]:
                tup_list[j], tup_list[j + 1] = swap (tup_list[j], tup_list[j + 1])
    return tup_list

# SJF
# Non-preemptive
def sjf_algorithm(process_info):
    timestamp = 0
    ready_queue = []
    gantt_chart = []
    bubble_sort_arrival(process_info)
    
    # Add processes into ready queue (based on arrival time) and add process into 'gantt chart' from ready queue (based on burst time)
    while len(process_info) != 0 or len(ready_queue) != 0:
        while len(process_info) != 0 and process_info[0][2] <= timestamp:
            ready_queue.append(process_info.pop(0))
        
        if len(ready_queue) != 0:
            bubble_sort_burst(ready_queue)
            current_process = ready_queue.pop(0)
            gantt_chart.append(current_process)
            timestamp += current_process[1]
        else:
            timestamp += 1

    print("Processes in order after SJF: ", [p[0] for p in gantt_chart])

# Test Cases for SJF
def test_sjf_algorithm():
    # Simulate user input
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "4",
            "Enter the burst time for P0: ": "6",
            "Enter the arrival time for P0: ": "0",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "8",
            "Enter the arrival time for P1: ": "0",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "7",
            "Enter the arrival time for P2: ": "0",
            "Enter the priority for P2: ": "3",
            "Enter the burst time for P3: ": "3",
            "Enter the arrival time for P3: ": "0",
            "Enter the priority for P3: ": "4",
        }
        return inputs[prompt]

    # Mock the input function
    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        # Get the number of processes
        num_processes = get_number_of_processes()
        # Get the process information
        process_info = get_process_info(num_processes)
        # Run the SJF algorithm
        sjf_algorithm(process_info)
    finally:
        # Restore the original input function
        __builtins__.input = original_input

def test_sjf_algorithm_different_arrival():
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "4",
            "Enter the burst time for P0: ": "6",
            "Enter the arrival time for P0: ": "2",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "8",
            "Enter the arrival time for P1: ": "0",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "7",
            "Enter the arrival time for P2: ": "1",
            "Enter the priority for P2: ": "3",
            "Enter the burst time for P3: ": "3",
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

def test_sjf_algorithm_same_arrival_burst():
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "4",
            "Enter the burst time for P0: ": "5",
            "Enter the arrival time for P0: ": "0",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "5",
            "Enter the arrival time for P1: ": "0",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "5",
            "Enter the arrival time for P2: ": "0",
            "Enter the priority for P2: ": "3",
            "Enter the burst time for P3: ": "5",
            "Enter the arrival time for P3: ": "0",
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

def test_sjf_algorithm_diff_burst_same_arrival():
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "4",
            "Enter the burst time for P0: ": "10",
            "Enter the arrival time for P0: ": "0",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "1",
            "Enter the arrival time for P1: ": "0",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "2",
            "Enter the arrival time for P2: ": "0",
            "Enter the priority for P2: ": "3",
            "Enter the burst time for P3: ": "3",
            "Enter the arrival time for P3: ": "0",
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

def test_sjf_algorithm_late_arrival():
    def mock_input(prompt):
        inputs = {
            "Enter the number of processes: ": "3",
            "Enter the burst time for P0: ": "4",
            "Enter the arrival time for P0: ": "5",
            "Enter the priority for P0: ": "1",
            "Enter the burst time for P1: ": "3",
            "Enter the arrival time for P1: ": "6",
            "Enter the priority for P1: ": "2",
            "Enter the burst time for P2: ": "2",
            "Enter the arrival time for P2: ": "7",
            "Enter the priority for P2: ": "3",
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

# Run the test cases
# test_sjf_algorithm()
test_sjf_algorithm_different_arrival()
test_sjf_algorithm_same_arrival_burst()
test_sjf_algorithm_diff_burst_same_arrival()
test_sjf_algorithm_late_arrival()


# SRT
    # Preemptive

#------------------------------------------------------------------------------------------------------------
# Main function
def main():
    numProcess = get_number_of_processes()
    timeQuantum = get_time_quantum()
    processInfo = get_process_info(numProcess)

    print("Number of processes: ", numProcess)
    print("Time quantum: ", timeQuantum)
    print("Process info: ", processInfo)

    sjf_algorithm(processInfo)

# main()




#------------------------------------------------------------------------------------------------------------


# After getting the process info, we can now display the process info in customtkinter

# Display the process info in customtkinter
# Initialize the main window
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("green")

# app = ctk.CTk()
# app.title("CPU Scheduling Simulator")
# app.geometry("800x500")

# header_label = ctk.CTkLabel(app, text="CPU Scheduling Simulator")
# header_label.grid(row=0, column=0, pady=20)

# # # Add a frame for the process info
# frame = ctk.CTkFrame(app)
# frame.grid(row=1, column=0, pady=10)

# Add a label for the process info
# label = ctk.CTkLabel(frame, text="Process Info")
# label.pack()

# Add a table view for the process info
# create a grid layout for the table view

# headers = ["Process", "Arrival Time", "Burst Time", "Priority"]
# rows = [["P0"], ["P1"], ["P2"]]

# for i, header in enumerate(headers):
#     ctk.CTkLabel(frame, text=header).grid(row=0, column=i)

# for i, row in enumerate(rows):
#     for j, cell in enumerate(row):
#         ctk.CTkLabel(frame, text=cell).grid(row=i+1, column=j)

#         # Add the process info to the table view
#         for i, process in enumerate(processInfo):
#             burst_time, arrival_time, priority = process
#             ctk.CTkLabel(frame, text=f"{i+1}").grid(row=i+1, column=0)
#             ctk.CTkLabel(frame, text=f"{burst_time}").grid(row=i+1, column=1)
#             ctk.CTkLabel(frame, text=f"{arrival_time}").grid(row=i+1, column=2)
#             ctk.CTkLabel(frame, text=f"{priority}").grid(row=i+1, column=3)


# app.mainloop()