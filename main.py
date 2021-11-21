# Importing random
import random

rock = '''0
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

# Write your code below this line 👇

# Getting input
player_choose = int(input("What do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors.\n"))

# Creating a variable to store players move
player_move = 0

# Matching the image with player's move
if player_choose == 0:
    player_move = rock
elif player_choose == 1:
    player_move = paper
elif player_choose == 2:
    player_move = scissors
else:
    print("Wrong input, please follow the instructions properly and give the correct input")

# Making computer to randomise rock or paper or scissors


computer_choose = random.randint(0, 2)
computer_move = 0
# Matching computer's choice with rock or paper or scissors
if computer_choose == 0:
    computer_move = rock
elif computer_choose == 1:
    computer_move = paper
else:
    computer_move = scissors

# Printing player's input
print(f"Your move is: \n   {player_move}")

# Printing computer's input
print(f"Computer's move is: \n   {computer_move}")

# Choosing the winner
# Condition for draw
if player_choose == computer_choose:
    print("Match draw.\n You both chose same.")
# Conditions for computer win or player loose
elif player_choose == 0 and computer_choose == 1:
    print("You lost the game. Computer won.")
elif player_choose == 2 and computer_choose == 0:
    print("You lost the game. Computer won.")
elif player_choose == 1 and computer_choose == 2:
    print("You lost the game. Computer won.")
# Conditions for player win or computer loose
elif player_choose == 0 and computer_choose == 2:
    print("You won the game. Computer lost.")
elif player_choose == 1 and computer_choose == 0:
    print("You won the game. Computer lost.")
elif player_choose == 2 and computer_choose == 1:
    print("You won the game. Computer lost.")
else:
    print("Something went wrong. Please try again.")
