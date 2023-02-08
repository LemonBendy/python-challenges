from tkinter import *

userForm = Tk()
userForm.title("Testing GUI")
userForm.geometry("70x200")
timerTicks = 0
timings1 = [0, 6, 9, 12]


def timer1():
    global timerTicks
    timerTicks += 1
    lblTimer.configure(text=timerTicks)
    setLights()
    userForm.after(400, timer1)


def setLights():
    global timerTicks
    if timerTicks > 18:
        timerTicks = 0
    elif timerTicks > 15:
        turnRedAmber(C, cRed, cAmber, cGreen)
        turnAmber(C2, c2Red, c2Amber, c2Green)
    elif timerTicks > 12:
        turnRed(C, cRed, cAmber, cGreen)
        turnGreen(C2, c2Red, c2Amber, c2Green)
    elif timerTicks > 6:
        turnAmber(C, cRed, cAmber, cGreen)
        turnRedAmber(C2, c2Red, c2Amber, c2Green)
    else:
        turnGreen(C, cRed, cAmber, cGreen)
        turnRed(C2, c2Red, c2Amber, c2Green)


def turnRed(C, cRed, cAmber, cGreen):
    C.itemconfig(cRed, fill=Lights[1])
    C.itemconfig(cAmber, fill=Lights[0])
    C.itemconfig(cGreen, fill=Lights[0])


def turnRedAmber(C, cRed, cAmber, cGreen):
    C.itemconfig(cRed, fill=Lights[1])
    C.itemconfig(cAmber, fill=Lights[2])
    C.itemconfig(cGreen, fill=Lights[0])


def turnAmber(C, cRed, cAmber, cGreen):
    C.itemconfig(cRed, fill=Lights[0])
    C.itemconfig(cAmber, fill=Lights[2])
    C.itemconfig(cGreen, fill=Lights[0])


def turnGreen(C, cRed, cAmber, cGreen):
    C.itemconfig(cRed, fill=Lights[0])
    C.itemconfig(cAmber, fill=Lights[0])
    C.itemconfig(cGreen, fill=Lights[3])


def turnOff(C, cRed, cAmber, cGreen):
    C.itemconfig(cRed, fill=Lights[0])
    C.itemconfig(cAmber, fill=Lights[0])
    C.itemconfig(cGreen, fill=Lights[0])


C = Canvas(userForm, bg="grey", height=170, width=70)
# coord = 10, 50, 240, 210
Top = 10
Left = 10
Size = 50
cRed = C.create_oval(Left, Top, Left + Size, Top + Size)
cAmber = C.create_oval(Left, Top + Size, Left + Size, Top + Size * 2)
cGreen = C.create_oval(Left, Top + Size * 2, Left + Size, Top + Size * 3)
C.pack()

Lights = {1: "red", 2: "yellow", 3: "green", 0: "black"}
turnOff(C, cRed, cAmber, cGreen)

C2 = Canvas(userForm, bg="grey", height=170, width=70)
# coord = 10, 50, 240, 210
Top2 = 10
Left2 = 10
Size2 = 50
c2Red = C2.create_oval(Left2, Top2, Left2 + Size2, Top2 + Size2)
c2Amber = C2.create_oval(Left2, Top2 + Size2, Left2 + Size2, Top2 + Size2 * 2)
c2Green = C2.create_oval(Left2, Top2 + Size2 * 2, Left2 + Size2, Top2 + Size2 * 3)
C2.pack()
turnOff(C2, c2Red, c2Amber, c2Green)

lblTimer = Label(userForm)
lblTimer.pack()
timer1()
userForm.mainloop()