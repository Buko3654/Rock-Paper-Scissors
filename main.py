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
  print(f"{rock}\nYou chose rock.")
elif player == 1:
  print(f"{paper}\nYou chose paper.")
elif player == 2:
  print(f"{scissors}\nYou chose scissors.")

npc = random.randint(0,2)

if npc == 0:
  print(f"{rock}\nYour opponent chose rock.")
elif npc == 1:
  print(f"{paper}\nYour opponent chose paper.")
elif npc == 2:
  print(f"{scissors}\nYour opponent chose scissors.")

if player == npc:
  print("\nIt's a draw. Play again!")
elif player == 0:
  if npc == 1:
    print("\nYou lose. Sorry. Try again.")
  if npc == 2:
    print("\nCongratulations! You win! Rematch?")
elif player == 1:
  if npc == 2:
    print("\nYou lose. Sorry. Try again.")
  if npc == 0:
    print("\nCongratulations! You win! Rematch?")
elif player == 2:
  if npc == 0:
    print("\nYou lose. Sorry. Try again.")
  if npc == 1:
    print("\nCongratulations! You win! Rematch?")
else:
  print("\nYou typed an invalid number. You lose. Try again!")