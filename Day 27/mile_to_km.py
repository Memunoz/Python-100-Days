from tkinter import *

windows = Tk()
windows.title("Miles to Km")
windows.config(padx=20, pady=20)
FONT = ("arial", 12, "bold")


def convert():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text=f"{km}")


equal_label = Label(text="Is equal to: ", font=FONT)
equal_label.grid(column=0, row=2)
equal_label.config(padx=10, pady=10)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=1)
miles_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=2)
km_label.config(padx=10, pady=10)


entry = Entry(font=FONT, width=10)
entry.grid(column=1, row=1)


result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=2)
result_label.config(padx=10, pady=10)

check_button = Button(text="Calculate", font=FONT, command=convert)
check_button.grid(column=1, row=3)

windows.mainloop()
