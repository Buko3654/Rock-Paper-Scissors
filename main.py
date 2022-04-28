rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

player_in = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

player = int(player_in)

if player == 0:
  print(f"You chose rock.\n{rock}")
elif player == 1:
  print(f"You chose paper.\n{paper}")
elif player == 2:
  print(f"You chose scissors.\n{scissors}")

choices = ["Rock", "Paper", "Scissors"]

npc = random.randint(0,2)

if npc == 0:
  print(f"Your opponent chose rock.\n{rock}")
elif npc == 1:
  print(f"Your opponent chose paper.\n{paper}")
elif npc == 2:
  print(f"Your opponent chose scissors.\n{scissors}")

if player == npc:
  print("It's a draw. Play again!")
elif player == 0:
  if npc == 1:
    print("You lose. Sorry. Try again.")
  if npc == 2:
    print("Congratulations! You win! Rematch?")
elif player == 1:
  if npc == 2:
    print("You lose. Sorry. Try again.")
  if npc == 0:
    print("Congratulations! You win! Rematch?")
elif player == 2:
  if npc == 0:
    print("You lose. Sorry. Try again.")
  if npc == 1:
    print("Congratulations! You win! Rematch?")