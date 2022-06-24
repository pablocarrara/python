import tkinter
import random
from tkinter import messagebox
from tkinter import END

low = 0
high = 20



rand = random.randint(low, high)

count = 0

def check(guess):
    global count
    count += 1

    if guess < rand:
        tkinter.Label(tk, text=f'{guess} is low').pack()
        entry.delete(0,END)
    elif guess > rand: 
        tkinter.Label(tk, text=f'{guess} is high').pack()
        entry.delete(0,END)
    else:
        tkinter.messagebox.showinfo('you win:', f'{guess} is correct. You made {count} attempts')
        
    





tk = tkinter.Tk()

tk.title("Guessing game")

guess_goal = tkinter.Label(tk, text= f"Guess a number from {low} to {high} (inclusive)")
guess_goal.pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text= "take a guess", command=lambda:check(int(entry.get())))
button.pack()

tk.mainloop()
















