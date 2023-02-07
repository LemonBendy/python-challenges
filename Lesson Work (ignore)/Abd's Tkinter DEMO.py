import tkinter
from tkinter import *


def back(wx):
    wx.destroy()
    main()


def main():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    win1 = Tk() #generate window
    win1.title("Welcome") # gives window title
    win1.geometry("400x200") # sets resolution/dimensions of window

    titleLabel = Label(win1, text=" Welcome to TKINTER programming") # Creates label for welcome
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10) # formats where the label is shown

    exitButton = Button(win1, text="Exit", width=12, command=quit) # creates a button for exiting
    exitButton.grid(row=1, column=0, padx=10, pady=30) # formats where the button is shown, (0,1)

    loginButton = Button(win1, text="Login", width=12, command=lambda: login(win1)) # creates a login button, passes the current window as a parameter to be destroyed when the next function is called.
    loginButton.grid(row=1, column=1, padx=10, pady=10) # formats where the button is shown, (1,1)

    signinButton = Button(win1, text="Sign in", width=12, command=lambda: signin(win1)) # creates a sign in button, passes the current window as a parameter to be destroyed when the next function is called.
    signinButton.grid(row=1, column=2, padx=10, pady=10) # formats where the button is shown, (2,1)

    mainloop() # loops the window


def login(w):
    w.destroy()
    win2 = Tk()
    win2.title("Sign in ... ")
    win2.geometry("400x180")

    titleLabel = Label(win2, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    backButton = Button(win2, text="Back", command=lambda: back(win2))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def signin(w):
    w.destroy()
    win3 = Tk()
    win3.title("Sign in ... ")
    win3.geometry("400x180")

    titleLabel = Label(win3, text=" Please complete all fields ")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3))
    backButton.grid(row=4, column=0, sticky="SNEW", padx=10, pady=10)

    mainloop()


def menu():
    # code for creating the application's menu

    pass


main()