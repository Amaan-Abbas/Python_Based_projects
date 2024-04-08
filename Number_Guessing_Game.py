import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class NumberGuessingGame:
    def __init__(silly, window):
        silly.window = window
        silly.window.title("Number Guessing Game")
        silly.username = tk.StringVar()
        silly.password = tk.StringVar()
        silly.originalpassword = "password"  # original login password
        silly.loginscreen()

    def loginscreen(silly):
        loginframe = tk.Frame(silly.window, bg="gray", borderwidth=10, relief="raised")
        loginframe.pack(padx=20, pady=20)

        tk.Label(loginframe, text="Enter username and password:", font="comicsansms 24 bold").grid(row=0, column=0, columnspan=2, padx=6, pady=6)

        tk.Label(loginframe, text="Username: ", font="comicsansms 19 bold", borderwidth=6, relief="raised").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(loginframe, textvariable=silly.username, font="comicsansms 19 bold").grid(row=1, column=1, padx=6, pady=6)

        tk.Label(loginframe, text="Password: ", font="comicsansms 19 bold", borderwidth=6, relief="raised").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(loginframe, textvariable=silly.password, show="*", font="comicsansms 19 bold", borderwidth=6, relief="raised").grid(row=2, column=1, padx=6, pady=6)

        tk.Button(loginframe, text="Login", command=silly.login).grid(row=3, column=0, columnspan=2, padx=6, pady=10)
        tk.Button(loginframe, text="Change Password", command=silly.changepassword).grid(row=4, column=0, columnspan=2, padx=6, pady=10)

    def login(silly):
        if silly.username.get() == "Admin" and silly.password.get() == silly.originalpassword:
            silly.intogamescreen()
        else:
            messagebox.showerror("Wrong Username or Password", "Try again.")

    def changepassword(silly):
        newpassword = simpledialog.askstring("Enter new password", "Enter new password:")
        if newpassword:
            silly.originalpassword = newpassword
            messagebox.showinfo("Password changed!", "Password has been changed successfully.")

    def intogamescreen(silly):
        gameframe = tk.Frame(silly.window, bg="gray", borderwidth=10, relief="raised")
        gameframe.pack(padx=20, pady=20)

        target = random.randint(1, 100)

        tk.Label(gameframe, text="Guess the number between 1 to 100: ", font="comicsansms 24 bold").grid(row=0, column=0, columnspan=2)

        guessinput = tk.Entry(gameframe, font="comicsansms 19 bold")
        guessinput.grid(row=1, column=0, padx=6, pady=6)

        def check():
            try:
                userinput = int(guessinput.get())
                if userinput == target:
                    messagebox.showinfo("Congratulations!", "You have guessed the correct number.")
                elif userinput < target:
                    messagebox.showinfo("Try Again", "Guessed number is \"BELOW\" the target number. Guess ABOVE!")
                else:
                    messagebox.showinfo("Try Again", "Guessed number is \"ABOVE\" the target number. Guess BELOW!")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")

        tk.Button(gameframe, text="Check", command=check).grid(row=1, column=1, columnspan=2, padx=6, pady=6)
    

if __name__ == "__main__":
    gameroot = tk.Tk()
    app = NumberGuessingGame(gameroot)
    gameroot.mainloop()
