from tkinter import *

root = Tk()
root.geometry("644x394")
root.title("Converter")

f1 = Frame(root, borderwidth=3).grid(row=0, column=0)
l = Label(f1, text="Feet To Meter", font=("CosmicSans", 30)).grid(row=0, column=3)

f2 = Frame(root, borderwidth=15).grid(row=2, column=2)
l1 = Label(f2, text="Feet : ", font=("CosmicSans", 20)).grid(row=2, column=2)
l2 = Label(f2, text="Meters : ", font=("CosmicSans", 20)).grid(row=3, column=2)
e1 = Entry(f2, width=15, borderwidth=5)
e2 = Entry(f2, width=15, borderwidth=5)

f=StringVar()

def calc():
    e2.delete(0,END)
    feet = e1.get()
    meter = float(feet) / (3.281)
    e2.insert(0, meter)

e1.grid(row=2, column=3)
e2.grid(row=3, column=3)

b = Button(f2, text="Calculate",command=calc).grid(row=4, column=3)

root.mainloop()
