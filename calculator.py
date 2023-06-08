import tkinter as tk

# Define the main window
root = tk.Tk()
root.title("Calculator")

# Define the entry box
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

# Define the buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20)
button_2 = tk.Button(root, text="2", padx=40, pady=20)
button_3 = tk.Button(root, text="3", padx=40, pady=20)
button_4 = tk.Button(root, text="4", padx=40, pady=20)
button_5 = tk.Button(root, text="5", padx=40, pady=20)
button_6 = tk.Button(root, text="6", padx=40, pady=20)
button_7 = tk.Button(root, text="7", padx=40, pady=20)
button_8 = tk.Button(root, text="8", padx=40, pady=20)
button_9 = tk.Button(root, text="9", padx=40, pady=20)
button_0 = tk.Button(root, text="0", padx=40, pady=20)
button_add = tk.Button(root, text="+", padx=39, pady=20)
button_equal = tk.Button(root, text="=", padx=91, pady=20)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20)
button_decimal = tk.Button(root, text=".", padx=40, pady=20)
button_negative = tk.Button(root, text="-", padx=40, pady=20)

# Define the button placement
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_negative.grid(row=4, column=0)

#Calculate the result
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

#Write the result
def button_add_click():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)
def button_equal_click():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    if math == "division":
        entry.insert(0, f_num / int(second_number))
def button_clear_click():
    entry.delete(0, tk.END)
def button_subtract_click():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, tk.END)
def button_multiply_click():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, tk.END)
def button_divide_click():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, tk.END)
def button_decimal_click():
    first_number = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, first_number + ".")
def button_negative_click():
    first_number = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, "-" + first_number)

# Define the button actions
button_1.configure(command=lambda: button_click(1))
button_2.configure(command=lambda: button_click(2))
button_3.configure(command=lambda: button_click(3))
button_4.configure(command=lambda: button_click(4))
button_5.configure(command=lambda: button_click(5))
button_6.configure(command=lambda: button_click(6))
button_7.configure(command=lambda: button_click(7))
button_8.configure(command=lambda: button_click(8))
button_9.configure(command=lambda: button_click(9))
button_0.configure(command=lambda: button_click(0))
button_add.configure(command=button_add_click)
button_equal.configure(command=button_equal_click)
button_clear.configure(command=button_clear_click)
button_negative.configure(command=button_subtract_click)

#Define the main loop
root.mainloop()
