from tkinter import *

windows = Tk()
windows.title("First GUI")
windows.minsize(width=500, height=300)
windows.config(padx=20, pady=20)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


my_label = Label(text="First Label", font=("arial", 24))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

my_button = Button(text="click me", command=button_clicked)
my_button.grid(column=1, row=1)
my_button.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=3, row=2)


new_button = Button(text="New_button")
new_button.grid(column=2, row=0)
new_button.config(padx=20, pady=20)

windows.mainloop()
