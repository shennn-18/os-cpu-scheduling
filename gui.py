# This is the GUI version of CPU Scheduling Algorithm based on CLI Version's Logic
# Flow:
    # User first enter number of processes and time quantum
        # Based on the number of processes, a pop-up window tells user to input 
        # the corresponding process' info (with a grid layout)
        # After submitting the info, the pop up window is closed
    # User click onto run CPU scheduling algorithm
        # 4 tabs will appear (based on algorithm)
            # each tab has their own table (ttk.treeview) to show process' info after
            # running the algorithm (completion time, TAT and WT etc)
            # Calculation of sum and average of TAT and WT are shown after the table
            # Gantt chart is drawn and displayed after the calculation info

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cli import sjf_algorithm, srt_algorithm

root = Tk()
root.title("CPU Scheduling Algorithm Simulator - OS")
root.geometry("1920x1080")
# root.attributes("-fullscreen", True)

# Create main canvas and scrollbar
main_canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=main_canvas.yview)
scrollable_frame = Frame(main_canvas)

#-------------------------------------------------------------------------------------
# SCROLLBAR
# Configure the canvas for scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
)
main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
main_canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
main_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#-------------------------------------------------------------------------------------
# FUNCTIONS

# Function for submit button
# When it's clicked, process info entries window will pop up
def submit_button_fun():
    create_process_info_window(num_process_entry.get())

# Run CPU Scheduling Algorithms (all of them)
# Create tabs for each algorithm (one tab for one algorithm)
# User able to switch between tabs to view how diff algorithm perform
def run_algorithm_fun():
    tabControl = ttk.Notebook(scrollable_frame)
    sjf_tab = Frame(tabControl)
    srt_tab = Frame(tabControl)
    pr_tab = Frame(tabControl)
    rr_tab = Frame(tabControl)

    tabControl.add(sjf_tab, text="SJF Algorithm", padding=20)
    tabControl.add(srt_tab, text="SRT Algorithm", padding=20)
    tabControl.add(pr_tab, text="Priority Algorithm", padding=20)
    tabControl.add(rr_tab, text="Round Robin Algorithm", padding=20)
    tabControl.grid(row=3, column=0, padx=50, pady=100)

    # Create Treeview for SJF tab
    sjf_tree = ttk.Treeview(sjf_tab, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
    sjf_tree.heading("Name", text="Name")
    sjf_tree.heading("Burst Time", text="Burst Time")
    sjf_tree.heading("Arrival Time", text="Arrival Time")
    sjf_tree.heading("Priority", text="Priority")
    sjf_tree.heading("Completion Time", text="Completion Time")
    sjf_tree.heading("Turnaround Time", text="Turnaround Time")
    sjf_tree.heading("Waiting Time", text="Waiting Time")
    sjf_tree.grid(row=1, column=0, padx=30, pady=30)

    # Create Treeview for SRT tab
    srt_tree = ttk.Treeview(srt_tab, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
    srt_tree.heading("Name", text="Name")
    srt_tree.heading("Burst Time", text="Burst Time")
    srt_tree.heading("Arrival Time", text="Arrival Time")
    srt_tree.heading("Priority", text="Priority")
    srt_tree.heading("Completion Time", text="Completion Time")
    srt_tree.heading("Turnaround Time", text="Turnaround Time")
    srt_tree.heading("Waiting Time", text="Waiting Time")
    srt_tree.grid(row=1, column=0, padx=30, pady=30)

    # Create Treeview for PR tab
    pr_tree = ttk.Treeview(pr_tab, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
    pr_tree.heading("Name", text="Name")
    pr_tree.heading("Burst Time", text="Burst Time")
    pr_tree.heading("Arrival Time", text="Arrival Time")
    pr_tree.heading("Priority", text="Priority")
    pr_tree.heading("Completion Time", text="Completion Time")
    pr_tree.heading("Turnaround Time", text="Turnaround Time")
    pr_tree.heading("Waiting Time", text="Waiting Time")
    pr_tree.grid(row=1, column=0, padx=30, pady=30)

    # Create Treeview for RR tab
    rr_tree = ttk.Treeview(rr_tab, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
    rr_tree.heading("Name", text="Name")
    rr_tree.heading("Burst Time", text="Burst Time")
    rr_tree.heading("Arrival Time", text="Arrival Time")
    rr_tree.heading("Priority", text="Priority")
    rr_tree.heading("Completion Time", text="Completion Time")
    rr_tree.heading("Turnaround Time", text="Turnaround Time")
    rr_tree.heading("Waiting Time", text="Waiting Time")
    rr_tree.grid(row=1, column=0, padx=30, pady=30)

    # Run SJF and SRT algorithms and display results
    sjf_process_info, sjf_gantt_chart = sjf_algorithm([(p['name'], p['burst'], p['arrival'], p['priority']) for p in process_info_data])
    srt_process_info, srt_gantt_chart = srt_algorithm([(p['name'], p['burst'], p['arrival'], p['priority']) for p in process_info_data])

    display_results(sjf_tree, sjf_process_info)
    display_results(srt_tree, srt_process_info)

    # Display calculation results for SJF
    sjf_tat_sum = sum([p[5] for p in sjf_process_info])
    sjf_wt_sum = sum([p[6] for p in sjf_process_info])
    sjf_tat_avg = round(sjf_tat_sum / len(sjf_process_info), 2)
    sjf_wt_avg = round(sjf_wt_sum / len(sjf_process_info), 2)

    Label(sjf_tab, text=f"Sum of Turnaround Time: {sjf_tat_sum}").grid(row=2, column=0, padx=30, pady=10)
    Label(sjf_tab, text=f"Average Turnaround Time: {sjf_tat_avg}").grid(row=3, column=0, padx=30, pady=10)
    Label(sjf_tab, text=f"Sum of Waiting Time: {sjf_wt_sum}").grid(row=4, column=0, padx=30, pady=10)
    Label(sjf_tab, text=f"Average Waiting Time: {sjf_wt_avg}").grid(row=5, column=0, padx=30, pady=10)
    Label(sjf_tab, text=f"Processes in order after SJF: {[p['name'] for p in sjf_gantt_chart]}").grid(row=6, column=0, padx=30, pady=10)

    # Display calculation results for SRT
    srt_tat_sum = sum([p[5] for p in srt_process_info])
    srt_wt_sum = sum([p[6] for p in srt_process_info])
    srt_tat_avg = round(srt_tat_sum / len(srt_process_info), 2)
    srt_wt_avg = round(srt_wt_sum / len(srt_process_info), 2)

    Label(srt_tab, text=f"Sum of Turnaround Time: {srt_tat_sum}").grid(row=2, column=0, padx=30, pady=10)
    Label(srt_tab, text=f"Average Turnaround Time: {srt_tat_avg}").grid(row=3, column=0, padx=30, pady=10)
    Label(srt_tab, text=f"Sum of Waiting Time: {srt_wt_sum}").grid(row=4, column=0, padx=30, pady=10)
    Label(srt_tab, text=f"Average Waiting Time: {srt_wt_avg}").grid(row=5, column=0, padx=30, pady=10)
    Label(srt_tab, text=f"Processes in order after SRT: {[p['name'] for p in srt_gantt_chart]}").grid(row=6, column=0, padx=30, pady=10)

#Display results in Treeview
def display_results(tree, results):
    for row in tree.get_children():
        tree.delete(row)
    for process in results:
        tree.insert("", "end", values=(process[0], process[1], process[2], process[3], process[4], process[5], process[6]))

# Process Info Window
# Based on number of processes, user can enter details like
# Burst time, arrival time and priority
def create_process_info_window(num_process):
    global process_info_window  # Make window global
    # Create top level
    process_info_window = Toplevel()
    process_info_window.title("Process Info Entries")
    process_info_window.geometry("500x400")

    num_process = int(num_process)
    count = 0

    process_info_entries_frame = LabelFrame(process_info_window, text="Process Info Entries")
    process_info_entries_frame.pack()

    p_label = Label(process_info_entries_frame, text="Processes")
    burst_time_label = Label(process_info_entries_frame, text="Burst Time")
    arrival_time_label = Label(process_info_entries_frame, text="Arrival Time")
    priority_label = Label(process_info_entries_frame, text="Priority")
    
    p_label.grid(row=0, column=0)
    burst_time_label.grid(row=0, column=1)
    arrival_time_label.grid(row=0, column=2)
    priority_label.grid(row=0, column=3, columnspan=4)

    while (count < num_process):
        process_label = Label(process_info_entries_frame, text="P" + str(count))
        burst_time_entries = Entry(process_info_entries_frame)
        arrival_time_entries = Entry(process_info_entries_frame)
        priority_entries = Entry(process_info_entries_frame)

        process_label.grid(row=count+1, column=0)
        burst_time_entries.grid(row=count+1, column=1)
        arrival_time_entries.grid(row=count+1, column=2)
        priority_entries.grid(row=count+1, column=3)

        count += 1

    submit_button = Button(process_info_window, text="Submit Process Info", command=submit_entries_fun)
    submit_button.pack()

# Save the entered info and close the process_info_window
def submit_entries_fun():
    global process_info_data, process_info_window
    process_info_data = []
    
    # Get all entries from the process info window
    entries_frame = process_info_window.winfo_children()[0]
    rows = (len(entries_frame.winfo_children()) - 4) // 4
    
    # Clear existing items in treeview
    for item in process_info_tree.get_children():
        process_info_tree.delete(item)
        
    # Collect and display data
    for i in range(rows):
        burst_time = entries_frame.grid_slaves(row=i+1, column=1)[0].get()
        arrival_time = entries_frame.grid_slaves(row=i+1, column=2)[0].get()
        priority = entries_frame.grid_slaves(row=i+1, column=3)[0].get()
        
        # Validate inputs
        try:
            burst_time = int(burst_time)
            arrival_time = int(arrival_time)
            priority = int(priority)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return
            
        process_data = {
            'name': f'P{i}',
            'burst': burst_time,
            'arrival': arrival_time,
            'priority': priority
        }
        process_info_data.append(process_data)
        
        # Insert into treeview
        process_info_tree.insert('', 'end', values=(f'P{i}', burst_time, arrival_time, priority))
    
    process_info_window.destroy()


#-------------------------------------------------------------------------------------
# WIDGETS

entries_frame = LabelFrame(scrollable_frame, text="Entries Frame", padx= 50, pady= 50)
entries_frame.grid()

num_process_label = Label(entries_frame, text="Number of Processes:   ")
num_process_entry = Entry(entries_frame, width=25, borderwidth=5)
time_quantum_label = Label(entries_frame, text="Time Quantum:   ")
time_quantum_entry = Entry(entries_frame, width=25, borderwidth=5)
submit_button = Button(entries_frame, text="Submit", command=submit_button_fun)
run_algorithm_button = Button(entries_frame, text="Run Algorithm", command=run_algorithm_fun)

num_process_label.grid(row=0, column=0)
num_process_entry.grid(row=0, column=1)
time_quantum_label.grid(row=1, column=0)
time_quantum_entry.grid(row=1, column=1)
submit_button.grid(row=2, column=0)
run_algorithm_button.grid(row=3, column=0)

# Create Process Info Display Frame
process_info_frame = LabelFrame(scrollable_frame, text="Process Information")
process_info_frame.grid(row=2, column=0, padx=50, pady=50)

# Create Treeview for initial process info display
process_info_data = []  # Global variable to store process info
process_info_tree = ttk.Treeview(process_info_frame, columns=("Process", "Burst Time", "Arrival Time", "Priority"), show='headings')
process_info_tree.heading("Process", text="Process")
process_info_tree.heading("Burst Time", text="Burst Time") 
process_info_tree.heading("Arrival Time", text="Arrival Time")
process_info_tree.heading("Priority", text="Priority")
process_info_tree.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()