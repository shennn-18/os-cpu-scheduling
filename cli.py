#CPU Scheduling downgraded version to CLI - as MVP
#Thoughts:
# User inputs everything
# User inputs the number of processes and time quantum (for Round Robin)
# User inputs the burst time, arrival time and priority for each process

import customtkinter as ctk
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
# format: burst time, arrival time, priority
def get_process_info(num_processes):
    process_info = []
    for i in range(num_processes):
        burst_time = int(input(f"Enter the burst time for process {i}: "))
        arrival_time = int(input(f"Enter the arrival time for process {i}: "))
        priority = int(input(f"Enter the priority for process {i}: "))
        process_info.append((burst_time, arrival_time, priority))
    return process_info

# Main function
numProcess = get_number_of_processes()
timeQuantum = get_time_quantum()
processInfo = get_process_info(numProcess)

print("Number of processes: ", numProcess)
print("Time quantum: ", timeQuantum)
print("Process info: ", processInfo)


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