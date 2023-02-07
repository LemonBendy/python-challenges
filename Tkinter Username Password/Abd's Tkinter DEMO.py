from tkinter import *
from tkinter import messagebox


def back(wx):
    wx.destroy()
    main()


def main():
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    win1 = Tk() #generate window
    win1.title("Welcome") # gives window title
    win1.geometry("400x180") # sets resolution/dimensions of window

    titleLabel = Label(win1, text=" Welcome to TKINTER programming") # Creates label for welcome
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10) # formats where the label is shown

    exitButton = Button(win1, text="Exit", width=12, command=lambda: quit()) # creates a button for exiting
    exitButton.grid(row=1, column=0, padx=10, pady=30) # formats where the button is shown, (0,1)

    loginButton = Button(win1, text="Login", width=12, command=lambda: login(win1)) # creates a login button, passes the current window as a parameter to be destroyed when the next function is called.
    loginButton.grid(row=1, column=1, padx=10, pady=10) # formats where the button is shown, (1,1)

    signupButton = Button(win1, text="Sign up", width=12, command=lambda: signup(win1)) # creates a sign in button, passes the current window as a parameter to be destroyed when the next function is called.
    signupButton.grid(row=1, column=2, padx=10, pady=10) # formats where the button is shown, (2,1)

    mainloop() # loops the window


def login(w):
    w.destroy()
    win2 = Tk()
    win2.title("Sign in: ")
    win2.geometry("400x200")

    backButton = Button(win2, text="Back", command=lambda: back(win2), width="5")
    backButton.grid(row=0, column=0, sticky="NW", padx=5, pady=10)

    usernameLabel = Label(win2, text="Username:")
    usernameLabel.grid(row=1, column=0, padx=10, pady=5, sticky="E")
    passwordLabel = Label(win2, text="Password:")
    passwordLabel.grid(row=2, column=0, padx=10, pady=5, sticky="E")

    username = Entry(win2, width="30")
    username.grid(row=1, column=1, padx=10, pady=5, sticky="W")
    password = Entry(win2, width="30")
    password.grid(row=2, column=1, padx=10, pady=5, sticky="W")

    exitButton = Button(win2, text="Exit", width="5", command=lambda: quit())  # creates a button for exiting
    exitButton.grid(row=4, column=0, padx=5, pady=10,  sticky="SW")

    mainloop()


def signup(w):
    w.destroy()
    win3 = Tk()
    win3.title("Sign up ... ")
    win3.geometry("400x200")

    usernameLabel = Label(win3, text="Username:")
    usernameLabel.grid(row=1, column=0, padx=10, pady=5, sticky="E")
    passwordLabel = Label(win3, text="Password:")
    passwordLabel.grid(row=2, column=0, padx=10, pady=5, sticky="E")
    reenterpasswordLabel = Label(win3, text="Reenter Password:")
    reenterpasswordLabel.grid(row=3, column=0, padx=5, pady=10, sticky="E")

    username = Entry(win3, width="30")
    username.grid(row=1, column=1, padx=10, pady=5, sticky="W")
    password = Entry(win3, width="30")
    password.grid(row=2, column=1, padx=10, pady=5, sticky="W")
    reenter = Entry(win3, width="30")
    reenter.grid(row=3, column=1, padx=10, pady=5, sticky="W")

    enterButton = Button(win3, text="Enter", command=lambda: signupcheck(win3, password, reenter, username))
    enterButton.grid(row=4, column=3, padx=10, pady=10)

    backButton = Button(win3, text="Back", command=lambda: back(win3), width="5")
    backButton.grid(row=0, column=0, sticky="NW", padx=5, pady=10)

    exitButton = Button(win3, text="Exit", width="5", command=lambda: quit())  # creates a button for exiting
    exitButton.grid(row=4, column=0, padx=5, pady=10,  sticky="SW")

    mainloop()


def signupcheck(f, p1, p2, user):
    p1 = str(p1.get())
    p2 = str(p2.get())
    user = str(user.get())
    if p1 == p2:
        with open("UsernameAndPassword.txt", "a") as f:
            f.write(f"{user} {p1}\n")
        f = open("UsernameAndPassword.txt", "r")
        print("CONTENTS", f.read())
        messagebox.showinfo(title="Complete", message="Account Created!")
    else:
        messagebox.showerror(title="Passwords are not the same", message="Make sure your passwords are the same")
        retry = messagebox.askretrycancel(title="Retry?", message="Would you like to retry?")
        if retry:
            signup(f)
        else:
            quit()

def menu(w):
    w.destroy()
    win4 = Tk()
    win4.title("Main Menu")
    win4.geometry("400x180")

    exitButton = Button(win4, text="Exit", width=12, command=quit)  # creates a button for exiting
    exitButton.grid(row=0, column=0, padx=10, pady=30)
    # code for creating the application's menu

    pass


main()