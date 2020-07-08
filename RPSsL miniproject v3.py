# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    if name == 'rock':
        name = 0
        return name
    
    elif name == 'Spock':
        name = 1
        return name
    
    elif name == 'paper':
        name = 2
        return name
    
    elif name == 'lizard':
        name = 3
        return name
    
    elif name == 'scissors':
        name = 4
        return name
    
    else:
        print('please try again using R,P,S,s, or L')
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "Not an appropriate answer" 
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print()
    # print out the message for the player's choice
    print(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("The computer chooses: " + comp_choice)
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number)%5
    # use if/elif/else to determine winner, print winner message
    if (difference == 1 or difference == 2):
        print("Computer wins! You will not fair well in the coming robot hegemony")
    elif (difference == 3 or difference == 4):
        print("You win! You will regret this")
    else:
        print("Tie! Appropriate...for now")
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


