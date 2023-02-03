from tkinter import *

def calculate(f, w, h):
    h = float(h.get())
    w = float(w.get())
    bmi = w/(h*h)
    bmi = round(bmi, 2)
    result = f"Your result is: {str(bmi)}"
    messagebox = Tk()
    messagebox.geometry("200x200")
    messagebox.title("BMI Value")
    messageboxLabel = Label(messagebox, text=result)
    messageboxLabel.grid(row=0, column=0, padx=10, pady=10, sticky="N")



def clearboxes(e1, e2):
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.focus()


def CreateWindow():
    window = Tk()
    window.title("BMI Calculator")
    window.geometry("500x220")
# creating welcome label
    welcomeLabel = Label(window, text="BMI Calculator!")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
# #  height and weight labels
    weightLabel = Label(window, text="Weight in Kg")
    weightLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    heightLabel = Label(window, text="Height in Metres")
    heightLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")
    helpLabel = Label(window, text="enter height(m)")
    helpLabel.grid(row=1, rowspan=2, column=2, padx=10, pady=10)
# #create entry boxes
    weightEntry = Entry(window, width="30")
    weightEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
    heightEntry = Entry(window, width="30")
    heightEntry.grid(row=2, column=1, padx=10, pady=10)
# #create the buttons
    exitButton = Button(window, text="Leave", width=12, command = quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10)
    clearButton = Button(window, text="Clear",width=12, command=lambda: clearboxes(weightEntry, heightEntry))
    clearButton.grid(row=3, column=1, padx=10, pady=10)
    calcButton = Button(window, text="Calculate", width=12, command=lambda: calculate(window, weightEntry, heightEntry))
    calcButton.grid(row=3, column=2, padx=10, pady=10)
    weightEntry.focus()
    window.mainloop()


CreateWindow()

