import customtkinter as ctk
import tkinter as tk

# Functions
# on click event
# def on_button_click(algorithm_name):
#     label.configure(text=f"{algorithm_name} is chosen")
#     print ("RadButton value: ", radio_var.get())

# Combobox event
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

#------------------------------------------------------------------------------------------------------------

# Initialize the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk() 
app.title("CPU Scheduling Simulator")
app.geometry("800x500")

#------------------------------------------------------------------------------------------------------------

# Add a label
header_label = ctk.CTkLabel(app, text="CPU Scheduling Simulator")
header_label.pack(pady=20)

# Add a frame with buttons
# frame = ctk.CTkFrame(app)
# frame.pack(pady=10)

# Add buttons to the frame
# radio_var = ctk.IntVar(value=0)

# radio_RR = ctk.CTkRadioButton(frame, text="Round Robin", command=lambda: on_button_click("Round Robin"), variable=radio_var, value=0)
# radio_RR.pack(side="left", padx=10)
# radio_NPP = ctk.CTkRadioButton(frame, text="Non-Preemptive Priority", command=lambda: on_button_click("Non-Preemptive Priority"), variable=radio_var, value=1)
# radio_NPP.pack(side="left", padx=10)
# radio_SJN = ctk.CTkRadioButton(frame, text="SJN", command=lambda: on_button_click("SJN"), variable=radio_var, value=2)
# radio_SJN.pack(side="left", padx=10)
# radio_SRT = ctk.CTkRadioButton(frame, text="SRT", command=lambda: on_button_click("SRT"), variable=radio_var, value=3)
# radio_SRT.pack(side="left", padx=10)

#------------------------------------------------------------------------------------------------------------

#INPUT FRAMES
# Number of processes, time quantum for initial input
# After initial input, the user will be able to input the burst time, arrival time and priority for each process
#

# Add another frame for the inputs
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=20)

# Add a label
label = ctk.CTkLabel(input_frame, text="Number of Processes: ")
label.pack()

# Add a combobox for selecting number of processes
num_processors_list = [str(i) for i in range(3, 11)]

combobox_var = ctk.StringVar(value="3")
combobox = ctk.CTkComboBox(input_frame, values=num_processors_list,
                                     command=combobox_callback, variable=combobox_var)
combobox_var.set("3")
combobox.pack(pady=20)

# Add a button to submit the number of processes
submit_button = ctk.CTkButton(input_frame, text="Submit")
submit_button.pack(pady=10)

#------------------------------------------------------------------------------------------------------------

# Run the application
app.mainloop()

