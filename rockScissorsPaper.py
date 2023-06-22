# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def userWon():
  print("The user won!")

def computerWon():
  print("The computer won!")

def whatIsIt(num):
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num + 1]

#gives back 1-3 at random
def computerChoice():
  return random.randint(1, 3)

def rockScissorsPaper():
  #Code here
  #ask user for a choice of rock scissor paper
  user_choice = input("Choose rock or scissors or paper: ")
  print(user_choice)

  # if statement that checks if user's user_choice is correct
  if user_choice == "Rock" or user_choice == "Scissors" or user_choice == "Paper":
    print("Your respose is valid")
  else:
    print("Your respose is not valid")
  
  #computer choice
  computer_choice = whatIsIt(computerChoice())
  print("computer choice: ")
  print(computer_choice)

  # print tie if user and computer respose is the same
  if user_choice == computer_choice:
    print("It's a tie!")
  else: 
    if user_choice == "Rock":
      if computer_choice == "Scissors":
        userWon()
      if computer_choice == "Paper":
        computerWon()
    elif user_choice == "Scissors":
      if computer_choice == "Paper":
        userWon()
      if computer_choice == "Rock":
        computerWon()
    elif user_choice == "Paper":
      if computer_choice == "Rock":
        userWon()
      if computer_choice == "Scissors":
        computerWon()

rockScissorsPaper()


