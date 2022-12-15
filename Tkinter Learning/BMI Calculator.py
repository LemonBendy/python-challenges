from tkinter import *


def main():
    window = Tk()
    window.title("First Window")
    window.geometry("420x420")
# create a label
    welcome = Label(window, text="Hello World!")
    welcome.grid(row=0, column=0, columnspan=3, sticky="W", padx=10
                 , pady=10)
    welcome.config(font=("Courier", 14), bg=("red"))
    mainloop()


main()
