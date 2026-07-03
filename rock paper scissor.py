from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

def play(user):
    computer = random.choice(["Rock", "Paper", "Scissors"])

    l1.config(text="You: " + user)
    l2.config(text="Computer: " + computer)

    if user == computer:
        l3.config(text="Tie")
    elif user == "Rock" and computer == "Scissors":
        l3.config(text="You Win")
    elif user == "Paper" and computer == "Rock":
        l3.config(text="You Win")
    elif user == "Scissors" and computer == "Paper":
        l3.config(text="You Win")
    else:
        l3.config(text="Computer Wins")

def reset():
    l1.config(text="You:")
    l2.config(text="Computer:")
    l3.config(text="")

Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=5)
Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=5)
Button(root, text="Scissors", command=lambda: play("Scissors")).pack(pady=5)

l1 = Label(root, text="You:")
l1.pack()

l2 = Label(root, text="Computer:")
l2.pack()

l3 = Label(root, text="", font=("Arial", 12))
l3.pack(pady=10)

Button(root, text="Restart", command=reset).pack()

root.mainloop()