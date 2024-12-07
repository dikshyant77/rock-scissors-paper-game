from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry('400x400')

label = Label(root, text="Choose between rock paper and scissors")

input_entry = Entry()


def rock_paper_scissors():

  opt = ('Rock', 'Paper', 'Scissors')
  global user_input
  user_input = str(input_entry.get())
  global computer_input
  computer_input = random.choice(opt)

  your_label = Label(root, text=f"You picked {user_input} !")
  your_label.pack()

  computer_label = Label(root, text=f"Computer picked {computer_input} !")
  computer_label.pack()

  if user_input == "Rock" and computer_input == "Scissors" or user_input == "rock" and computer_input == "Scissors":
    outcome = "You won"
  elif user_input == "Paper" and computer_input == "Rock" or user_input == "paper" and computer_input == "Rock":
    outcome = "You won"
  elif user_input == "Scissors" and computer_input == "Paper" or \
     user_input == "scissors" and computer_input == "Paper":
    outcome = "You won"
  elif user_input == computer_input:
   outcome = "It's a tie"
  outcome_label = Label(root, text = str(outcome))    
  outcome_label.pack()


btn_play = Button(root,
                  text="Play!",
                  command=rock_paper_scissors,
                  bg='black',
                  fg='white')

label.pack()

input_entry.pack()

btn_play.pack()

root.mainloop()