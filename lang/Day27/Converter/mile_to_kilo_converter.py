from tkinter import *


def calculate():
    km = round(float(miles.get()) * 1.609)
    res_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=120)
window.config(padx=20, pady=20)

# Miles input
miles = Entry(width=8, justify="center")
miles.grid(column=1, row=0)

# create label
label = Label(text="Miles", font=("Arial", 14))
label.grid(column=2, row=0)

# Is equal to label
iet_label = Label(text="is equal to", font=("Arial", 14))
iet_label.grid(column=0, row=1)

# Result label
res_label = Label(text="0", font=("Arial", 14))
res_label.grid(column=1, row=1)

# KM label
km_label = Label(text="Km", font=("Arial", 14))
km_label.grid(column=2, row=1)

# Calculate button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()