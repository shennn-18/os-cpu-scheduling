import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class SchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Algorithms")

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Input Frame
        self.input_frame = tk.Frame(self.scrollable_frame)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Number of Processes:").grid(row=0, column=0, padx=5, pady=5)
        self.num_processes = tk.Entry(self.input_frame)
        self.num_processes.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Time Quantum:").grid(row=1, column=0, padx=5, pady=5)
        self.time_quantum = tk.Entry(self.input_frame)
        self.time_quantum.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Initial Process Info Table Frame
        self.initial_table_frame = tk.Frame(self.scrollable_frame)
        self.initial_table_frame.pack(pady=10)

        self.initial_tree = ttk.Treeview(self.initial_table_frame, columns=("Name", "Burst Time", "Arrival Time", "Priority"), show='headings')
        self.initial_tree.heading("Name", text="Name")
        self.initial_tree.heading("Burst Time", text="Burst Time")
        self.initial_tree.heading("Arrival Time", text="Arrival Time")
        self.initial_tree.heading("Priority", text="Priority")
        self.initial_tree.pack(fill=tk.BOTH, expand=True)

        # SJF Table Frame
        self.sjf_table_frame = tk.Frame(self.scrollable_frame)
        self.sjf_table_frame.pack(pady=10)

        tk.Label(self.sjf_table_frame, text="SJF Algorithm Results").pack()
        self.sjf_tree = ttk.Treeview(self.sjf_table_frame, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
        self.sjf_tree.heading("Name", text="Name")
        self.sjf_tree.heading("Burst Time", text="Burst Time")
        self.sjf_tree.heading("Arrival Time", text="Arrival Time")
        self.sjf_tree.heading("Priority", text="Priority")
        self.sjf_tree.heading("Completion Time", text="Completion Time")
        self.sjf_tree.heading("Turnaround Time", text="Turnaround Time")
        self.sjf_tree.heading("Waiting Time", text="Waiting Time")
        self.sjf_tree.pack(fill=tk.BOTH, expand=True)

        self.sjf_stats = tk.Label(self.sjf_table_frame, text="")
        self.sjf_stats.pack()

        # SRT Table Frame
        self.srt_table_frame = tk.Frame(self.scrollable_frame)
        self.srt_table_frame.pack(pady=10)

        tk.Label(self.srt_table_frame, text="SRT Algorithm Results").pack()
        self.srt_tree = ttk.Treeview(self.srt_table_frame, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
        self.srt_tree.heading("Name", text="Name")
        self.srt_tree.heading("Burst Time", text="Burst Time")
        self.srt_tree.heading("Arrival Time", text="Arrival Time")
        self.srt_tree.heading("Priority", text="Priority")
        self.srt_tree.heading("Completion Time", text="Completion Time")
        self.srt_tree.heading("Turnaround Time", text="Turnaround Time")
        self.srt_tree.heading("Waiting Time", text="Waiting Time")
        self.srt_tree.pack(fill=tk.BOTH, expand=True)

        self.srt_stats = tk.Label(self.srt_table_frame, text="")
        self.srt_stats.pack()

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.scrollable_frame)
        self.buttons_frame.pack(pady=10)

        self.run_button = tk.Button(self.buttons_frame, text="Run CPU Scheduling Algorithm", command=self.run_algorithms)
        self.run_button.grid(row=0, column=0, padx=5, pady=5)

        self.initial_process_info = []

    def submit(self):
        num_processes = int(self.num_processes.get())
        self.process_info = []

        # Create a new popup window for process input
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Enter Process Information")

        tk.Label(self.popup, text="Process").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.popup, text="Burst Time").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.popup, text="Arrival Time").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.popup, text="Priority").grid(row=0, column=3, padx=5, pady=5)

        self.entries = []
        for i in range(num_processes):
            tk.Label(self.popup, text=f"P{i}").grid(row=i+1, column=0, padx=5, pady=5)
            burst_time = tk.Entry(self.popup)
            burst_time.grid(row=i+1, column=1, padx=5, pady=5)
            arrival_time = tk.Entry(self.popup)
            arrival_time.grid(row=i+1, column=2, padx=5, pady=5)
            priority = tk.Entry(self.popup)
            priority.grid(row=i+1, column=3, padx=5, pady=5)
            self.entries.append((burst_time, arrival_time, priority))

        self.submit_process_button = tk.Button(self.popup, text="Submit", command=self.submit_process_info)
        self.submit_process_button.grid(row=num_processes+1, column=0, columnspan=4, pady=10)

    def submit_process_info(self):
        self.process_info = []
        for i, (burst_time, arrival_time, priority) in enumerate(self.entries):
            self.process_info.append((f"P{i}", int(burst_time.get()), int(arrival_time.get()), int(priority.get())))
        self.initial_process_info = self.process_info.copy()  # Store the initial process info
        self.popup.destroy()
        self.display_initial_process_info()

    def display_initial_process_info(self):
        for row in self.initial_tree.get_children():
            self.initial_tree.delete(row)
        for process in self.process_info:
            self.initial_tree.insert("", "end", values=process)

    def run_algorithms(self):
        self.process_info = self.initial_process_info.copy()  # Reset process_info to initial state
        sjf_result = sjf_algorithm(self.process_info.copy())
        srt_result = srt_algorithm(self.process_info.copy())
        self.display_results(sjf_result, srt_result)

    def display_results(self, sjf_result, srt_result):
        for row in self.sjf_tree.get_children():
            self.sjf_tree.delete(row)
        for row in self.srt_tree.get_children():
            self.srt_tree.delete(row)

        for process in sjf_result:
            self.sjf_tree.insert("", "end", values=(process[0], process[1], process[2], process[3], process[4], process[5], process[6]))

        for process in srt_result:
            self.srt_tree.insert("", "end", values=(process[0], process[1], process[2], process[3], process[4], process[5], process[6]))

        # Calculate and display average turnaround time and waiting time for SJF
        sjf_turnaround_times = [p[5] for p in sjf_result]
        sjf_waiting_times = [p[6] for p in sjf_result]
        sjf_avg_turnaround_time = avr_tat_cal(sjf_turnaround_times)
        sjf_avg_waiting_time = avr_wt_cal(sjf_waiting_times)
        sjf_total_turnaround_time = sum(sjf_turnaround_times)
        sjf_total_waiting_time = sum(sjf_waiting_times)

        self.sjf_stats.config(text=f"SJF - Total Turnaround Time: {sjf_total_turnaround_time}, Average Turnaround Time: {sjf_avg_turnaround_time}\n"
                                   f"Total Waiting Time: {sjf_total_waiting_time}, Average Waiting Time: {sjf_avg_waiting_time}")

        # Calculate and display average turnaround time and waiting time for SRT
        srt_turnaround_times = [p[5] for p in srt_result]
        srt_waiting_times = [p[6] for p in srt_result]
        srt_avg_turnaround_time = avr_tat_cal(srt_turnaround_times)
        srt_avg_waiting_time = avr_wt_cal(srt_waiting_times)
        srt_total_turnaround_time = sum(srt_turnaround_times)
        srt_total_waiting_time = sum(srt_waiting_times)

        self.srt_stats.config(text=f"SRT - Total Turnaround Time: {srt_total_turnaround_time}, Average Turnaround Time: {srt_avg_turnaround_time}\n"
                                   f"Total Waiting Time: {srt_total_waiting_time}, Average Waiting Time: {srt_avg_waiting_time}")

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
        for i, p in enumerate(process_info):
            if p[0] == process['name']:
                process_info[i] = (p[0], p[1], p[2], p[3], process['completion'], process['turnaround'], process['waiting'])

    return process_info

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
                # If we just switched processes, record in Gantt chart if not already recorded
                if not previous_process or current_process['name'] != previous_process['name']:
                    if not gantt_chart or gantt_chart[-1]['name'] != current_process['name']:
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
        for i, p in enumerate(process_info):
            if p[0] == process['name']:
                process_info[i] = (p[0], p[1], p[2], p[3], process['completion'], process['turnaround'], process['waiting'])

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

def avr_tat_cal(tat_list):
    """
    Calculate and return the average turnaround time.
    """
    total_tat = sum(tat_list)
    avr_tat = total_tat / len(tat_list)
    avr_tat = round(avr_tat, 2)
    return avr_tat

def avr_wt_cal(wt_list):
    """
    Calculate and return the average waiting time.
    """
    total_wt = sum(wt_list)
    avr_wt = total_wt / len(wt_list)
    avr_wt = round(avr_wt, 2)
    return avr_wt

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()