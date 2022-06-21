# This is a simple code for Rock Scissor Paper Game

# Imports

import random

# Variable declaration with ASCII grafiti

rock = ''' 
        _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)

'''

scissor = '''
    ____________
      ---'   ____)____
                ______)
             __________)
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
# ASCII list
weapons = [rock, scissor, paper]

# Weapon name list
weapons_name = ['Rock','Scissor','Paper']

# Game logic

# Ask user input
player_choice = int(input("Please enter 0 for Rock, 1 for Scissor and 2 for Paper ---> "))
player_weapon = weapons[player_choice]
player_weapon_name = weapons_name[player_choice]
print( f"You have chosen : {player_weapon_name} " )
print(player_weapon)

# Computer's Choice
comp_weapon = random.choice(weapons)
comp_weapon_name = weapons_name[(weapons.index(comp_weapon))]
print(f"Computer chose : {comp_weapon_name} ")
print(comp_weapon)

# Winner logic
if player_weapon_name == comp_weapon_name:
    print("It's a Draw !")
elif player_weapon_name == 'Rock' and comp_weapon_name == 'Scissor':
    print("You won !")
elif player_weapon_name == 'Paper' and comp_weapon_name == 'Rock':
    print("You won !")
elif player_weapon_name == 'Scissor' and comp_weapon_name == 'Paper':
    print("You won !")
else:
    print(" You Lost !, Try again..")









