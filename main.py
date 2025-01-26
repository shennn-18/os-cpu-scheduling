#-------------------------------------------------------------------------------------
# IMPORTS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#-------------------------------------------------------------------------------------
# MAIN APPLICATION CLASS
class CPUSchedulingSimulator:
    """
    Main application class that handles the CPU scheduling simulation GUI.
    Contains all UI elements and algorithm implementations.
    """
    
    def __init__(self, root):
        """Initialize the main window and setup the UI"""
        self.root = root
        self.root.title("CPU Scheduling Algorithm Simulator - OS")
        self.root.geometry("1000x600")
        self.process_info_data = []

        self.setup_ui()

    #-------------------------------------------------------------------------------------
    # UI SETUP AND MANAGEMENT
    def setup_ui(self):
        """Setup all UI components including main canvas, scrollbar, and entry fields"""
        main_canvas = Canvas(self.root)
        scrollbar = Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = Frame(main_canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)

        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        entries_frame = LabelFrame(scrollable_frame, text="Entries Frame", padx=50, pady=50)
        entries_frame.grid()

        num_process_label = Label(entries_frame, text="Number of Processes:   ")
        self.num_process_entry = Entry(entries_frame, width=25, borderwidth=5)
        time_quantum_label = Label(entries_frame, text="Time Quantum:   ")
        self.time_quantum_entry = Entry(entries_frame, width=25, borderwidth=5)
        submit_button = Button(entries_frame, text="Submit", command=self.submit_button_fun)
        run_algorithm_button = Button(entries_frame, text="Run Algorithm", command=self.run_algorithm_fun)

        num_process_label.grid(row=0, column=0)
        self.num_process_entry.grid(row=0, column=1)
        time_quantum_label.grid(row=1, column=0)
        self.time_quantum_entry.grid(row=1, column=1)
        submit_button.grid(row=2, column=0)
        run_algorithm_button.grid(row=3, column=0)

        process_info_frame = LabelFrame(scrollable_frame, text="Process Information")
        process_info_frame.grid(row=2, column=0, padx=50, pady=50)

        self.process_info_tree = ttk.Treeview(process_info_frame, columns=("Process", "Burst Time", "Arrival Time", "Priority"), show='headings')
        self.process_info_tree.heading("Process", text="Process")
        self.process_info_tree.heading("Burst Time", text="Burst Time")
        self.process_info_tree.heading("Arrival Time", text="Arrival Time")
        self.process_info_tree.heading("Priority", text="Priority")
        self.process_info_tree.pack(padx=10, pady=10, fill='both', expand=True)

    def submit_button_fun(self):
        """Handle submit button click - opens process info entry window"""
        # Validate that both fields are filled
        if not self.num_process_entry.get() or not self.time_quantum_entry.get():
            messagebox.showerror("Error", "Please fill in both Number of Processes and Time Quantum")
            return

        try:
            num_processes = int(self.num_process_entry.get())
            time_quantum = int(self.time_quantum_entry.get())
            
            # Validate number of processes
            if num_processes < 3 or num_processes > 10:
                messagebox.showerror("Error", "Number of processes must be between 3 and 10")
                return
            
            # Validate time quantum is positive
            if time_quantum <= 0:
                messagebox.showerror("Error", "Time quantum must be greater than 0")
                return

            self.time_quantum = time_quantum  # Store time quantum for later use
            self.create_process_info_window(num_processes)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return

    def create_process_info_window(self, num_process):
        """Create popup window for entering process information"""
        self.process_info_window = Toplevel()
        self.process_info_window.title("Process Info Entries")
        self.process_info_window.geometry("500x400")

        # Validate number of processes again as a safeguard
        if not (3 <= num_process <= 10):
            messagebox.showerror("Error", "Number of processes must be between 3 and 10")
            self.process_info_window.destroy()
            return

        num_process = int(num_process)
        count = 0

        process_info_entries_frame = LabelFrame(self.process_info_window, text="Process Info Entries")
        process_info_entries_frame.pack()

        p_label = Label(process_info_entries_frame, text="Processes")
        burst_time_label = Label(process_info_entries_frame, text="Burst Time")
        arrival_time_label = Label(process_info_entries_frame, text="Arrival Time")
        priority_label = Label(process_info_entries_frame, text="Priority")

        p_label.grid(row=0, column=0)
        burst_time_label.grid(row=0, column=1)
        arrival_time_label.grid(row=0, column=2)
        priority_label.grid(row=0, column=3, columnspan=4)

        while count < num_process:
            process_label = Label(process_info_entries_frame, text="P" + str(count))
            burst_time_entries = Entry(process_info_entries_frame)
            arrival_time_entries = Entry(process_info_entries_frame)
            priority_entries = Entry(process_info_entries_frame)

            process_label.grid(row=count + 1, column=0)
            burst_time_entries.grid(row=count + 1, column=1)
            arrival_time_entries.grid(row=count + 1, column=2)
            priority_entries.grid(row=count + 1, column=3)

            count += 1

        submit_button = Button(self.process_info_window, text="Submit Process Info", command=self.submit_entries_fun)
        submit_button.pack()

    def submit_entries_fun(self):
        """Handle process information submission and validation"""
        self.process_info_data = []

        entries_frame = self.process_info_window.winfo_children()[0]
        rows = (len(entries_frame.winfo_children()) - 4) // 4

        for item in self.process_info_tree.get_children():
            self.process_info_tree.delete(item)

        for i in range(rows):
            burst_time = entries_frame.grid_slaves(row=i + 1, column=1)[0].get()
            arrival_time = entries_frame.grid_slaves(row=i + 1, column=2)[0].get()
            priority = entries_frame.grid_slaves(row=i + 1, column=3)[0].get()

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
            self.process_info_data.append(process_data)
            self.process_info_tree.insert('', 'end', values=(f'P{i}', burst_time, arrival_time, priority))

        self.process_info_window.destroy()

    #-------------------------------------------------------------------------------------
    # ALGORITHM EXECUTION AND DISPLAY
    def run_algorithm_fun(self):
        """
        Create new window for algorithm results and execute all scheduling algorithms
        This is where you can add new algorithm tabs
        """
        algorithm_window = Toplevel(self.root)
        algorithm_window.title("CPU Scheduling Algorithm Results")
        algorithm_window.geometry("1200x800")

        tabControl = ttk.Notebook(algorithm_window)
        sjf_tab = Frame(tabControl)
        srt_tab = Frame(tabControl)
        pr_tab = Frame(tabControl)
        rr_tab = Frame(tabControl)

        tabControl.add(sjf_tab, text="SJF Algorithm", padding=20)
        tabControl.add(srt_tab, text="SRT Algorithm", padding=20)
        tabControl.add(pr_tab, text="Priority Algorithm", padding=20)
        tabControl.add(rr_tab, text="Round Robin Algorithm", padding=20)
        tabControl.pack(expand=1, fill="both")

        sjf_tree = self.create_treeview(sjf_tab)
        srt_tree = self.create_treeview(srt_tab)
        pr_tree = self.create_treeview(pr_tab)
        rr_tree = self.create_treeview(rr_tab)

        sjf_process_info, sjf_gantt_chart = self.sjf_algorithm([(p['name'], p['burst'], p['arrival'], p['priority']) for p in self.process_info_data])
        srt_process_info, srt_gantt_chart = self.srt_algorithm([(p['name'], p['burst'], p['arrival'], p['priority']) for p in self.process_info_data])

        self.display_results(sjf_tree, sjf_process_info)
        self.display_results(srt_tree, srt_process_info)

        self.display_calculation_results(sjf_tab, sjf_process_info, sjf_gantt_chart, "SJF")
        self.display_calculation_results(srt_tab, srt_process_info, srt_gantt_chart, "SRT")

    def create_treeview(self, parent):
        """
        Create a treeview to display process information
        Modify this to add new columns for additional process attributes
        """
        tree = ttk.Treeview(parent, columns=("Name", "Burst Time", "Arrival Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"), show='headings')
        tree.heading("Name", text="Name")
        tree.heading("Burst Time", text="Burst Time")
        tree.heading("Arrival Time", text="Arrival Time")
        tree.heading("Priority", text="Priority")
        tree.heading("Completion Time", text="Completion Time")
        tree.heading("Turnaround Time", text="Turnaround Time")
        tree.heading("Waiting Time", text="Waiting Time")
        tree.grid(row=1, column=0, padx=30, pady=30)
        return tree

    def display_results(self, tree, results):
        """Display algorithm results in the treeview"""
        for row in tree.get_children():
            tree.delete(row)
        for process in results:
            tree.insert("", "end", values=(process[0], process[1], process[2], process[3], process[4], process[5], process[6]))

    def display_calculation_results(self, tab, process_info, gantt_chart, algorithm_name):
        """
        Display calculation results and Gantt chart
        Extend this to show additional metrics
        """
        tat_sum = sum([p[5] for p in process_info])
        wt_sum = sum([p[6] for p in process_info])
        tat_avg = round(tat_sum / len(process_info), 2)
        wt_avg = round(wt_sum / len(process_info), 2)

        Label(tab, text=f"Sum of Turnaround Time: {tat_sum}").grid(row=2, column=0, padx=30, pady=10)
        Label(tab, text=f"Average Turnaround Time: {tat_avg}").grid(row=3, column=0, padx=30, pady=10)
        Label(tab, text=f"Sum of Waiting Time: {wt_sum}").grid(row=4, column=0, padx=30, pady=10)
        Label(tab, text=f"Average Waiting Time: {wt_avg}").grid(row=5, column=0, padx=30, pady=10)

        canvas = Canvas(tab, width=1000, height=200, bg="white")
        canvas.grid(row=7, column=0, padx=30, pady=30)
        max_time = max([segment[1] for segment in gantt_chart])
        self.draw_gantt_chart(canvas, gantt_chart, max_time)

    def draw_gantt_chart(self, canvas, gantt_chart, max_time):
        """
        Draw the Gantt chart visualization
        Modify this to change the chart appearance or add new features
        """
        canvas_width = 800
        scale = canvas_width / max_time
        x_offset = (1000 - canvas_width) / 2
        canvas_height = 200
        rect_height = 50
        y_start = (canvas_height - rect_height) / 2
        y_end = y_start + rect_height
        text_y = y_end + 10

        for process in gantt_chart:
            start_time = process[0]
            end_time = process[1]
            name = process[2]
            canvas.create_rectangle(start_time * scale + x_offset, y_start, end_time * scale + x_offset, y_end, fill="blue")
            canvas.create_text((start_time * scale + end_time * scale) / 2 + x_offset, (y_start + y_end) / 2, text=name, fill="white")
            canvas.create_text(start_time * scale + x_offset, text_y, text=str(start_time), anchor="n")
            canvas.create_text(end_time * scale + x_offset, text_y, text=str(end_time), anchor="n")

    #-------------------------------------------------------------------------------------
    # SCHEDULING ALGORITHMS
    def sjf_algorithm(self, process_info):
        """
        Shortest Job First (Non-preemptive) implementation
        Returns: tuple(process_info, execution_segments)
        """
        timestamp = 0
        ready_queue = []
        gantt_chart = []
        execution_segments = []

        processes = []
        for p in process_info:
            processes.append({
                'name': p[0],
                'burst': p[1],
                'arrival': p[2],
                'priority': p[3],
                'completion': 0,
                'turnaround': 0,
                'waiting': 0,
                'segments': []
            })

        processes.sort(key=lambda x: x['arrival'])

        while len(processes) != 0 or len(ready_queue) != 0:
            while len(processes) != 0 and processes[0]['arrival'] <= timestamp:
                ready_queue.append(processes.pop(0))

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x['burst'])
                current_process = ready_queue.pop(0)
                gantt_chart.append(current_process)
                execution_segments.append((timestamp, timestamp + current_process['burst'], current_process['name']))

                start_time = timestamp
                timestamp += current_process['burst']
                finish_time = timestamp

                current_process['completion'] = finish_time
                current_process['turnaround'] = finish_time - current_process['arrival']
                current_process['waiting'] = current_process['turnaround'] - current_process['burst']
            else:
                timestamp += 1

        for process in gantt_chart:
            for i, p in enumerate(process_info):
                if p[0] == process['name']:
                    process_info[i] = p + (process['completion'], process['turnaround'], process['waiting'])

        return process_info, execution_segments

    def srt_algorithm(self, process_info):
        """
        Shortest Remaining Time (Preemptive) implementation
        Returns: tuple(process_info, execution_segments)
        """
        timestamp = 0
        ready_queue = []
        gantt_chart = []
        execution_segments = []

        processes = []
        for p in process_info:
            processes.append({
                'name': p[0],
                'original_burst': p[1],
                'burst': p[1],
                'arrival': p[2],
                'priority': p[3],
                'completion': 0,
                'turnaround': 0,
                'waiting': 0,
                'segments': []
            })

        processes.sort(key=lambda x: x['arrival'])
        previous_process = None

        while len(processes) or len(ready_queue):
            while processes and processes[0]['arrival'] <= timestamp:
                ready_queue.append(processes.pop(0))

            if ready_queue:
                ready_queue.sort(key=lambda x: x['burst'])
                current_process = ready_queue[0]
                if current_process['burst'] == 0:
                    current_process['completion'] = timestamp
                    current_process['turnaround'] = timestamp - current_process['arrival']
                    current_process['waiting'] = current_process['turnaround'] - current_process['original_burst']
                    ready_queue.pop(0)
                else:
                    if not previous_process or current_process['name'] != previous_process['name']:
                        if previous_process:
                            previous_process['segments'][-1] = (previous_process['segments'][-1][0], timestamp)
                        current_process['segments'].append((timestamp, None))
                        if not gantt_chart or gantt_chart[-1]['name'] != current_process['name']:
                            gantt_chart.append(current_process)
                    current_process['burst'] -= 1
                    previous_process = current_process
                    timestamp += 1
            else:
                if processes:
                    timestamp = processes[0]['arrival']
                else:
                    timestamp += 1

        if previous_process:
            previous_process['segments'][-1] = (previous_process['segments'][-1][0], timestamp)

        for process in gantt_chart:
            for i, p in enumerate(process_info):
                if p[0] == process['name']:
                    segments = [(start, end if end is not None else timestamp) for start, end in process['segments']]
                    process_info[i] = p + (process['completion'], process['turnaround'], process['waiting'], segments)
                    execution_segments.extend([(start, end, process['name']) for start, end in segments])

        return process_info, execution_segments

    # TODO: Add more scheduling algorithms here
    # def non_preemptive_priority_algorithm(self, process_info):
    #     """Priority scheduling implementation"""
    #     pass

    # def round_robin_algorithm(self, process_info, time_quantum):
    #     """Round Robin implementation"""
    #     pass

#-------------------------------------------------------------------------------------
# MAIN ENTRY POINT
if __name__ == "__main__":
    root = Tk()
    app = CPUSchedulingSimulator(root)
    root.mainloop()