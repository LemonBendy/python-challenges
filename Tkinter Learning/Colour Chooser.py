import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk

root = tk.Tk()
root.title('Colour Chooser')
root.geometry('300x150')


def change_colour():
    colours = askcolor(title="Colour Chooser")
    root.configure(bg=colors[1])


ttk.Button(root, text="Select A Colour", command=lambda: change_colour).pack(expand=True)


root.mainloop()
