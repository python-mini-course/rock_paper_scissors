# Helper Functions
import random

def whatIsIt(num):
  choices = ["Rock", "Paper", "Scissors"]
  return choices[num - 1]

#gives back 0-2 at random
def generateComputerChoice():
  return random.randint(1, 3)