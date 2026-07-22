import tkinter as tk
from time import strftime 
# root window
root = tk.Tk()
root.title("Digital Clock")

def time():
    # 24-hour with seconds and date on next line
    string = strftime("%H:%M:%S %p \n%d-%m-%Y")
    label.config(text=string)
    label.after(1000, time)

# fixed font tuple and color option names
label = tk.Label(root, font=("Calibri", 50, "bold"), bg="yellow", fg="black")
label.pack(anchor='center')

time()

root.mainloop()

