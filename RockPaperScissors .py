#Libraries / Modules imports:

import keyboard
import random

player: str

#defining the functions: 

names: dict =  {
    "1" : "Rock",
    "2" : "Paper",
    "3" : "Scissors"}

def main_menu():
    logo()
    print("Press 'shift' to play")
    keyboard.wait('shift')
    choice()

def logo():
    print("\n--------------------")
    print("Rock Paper Scissors")
    print("--------------------\n")

def choice():
    player = str(input("\nType '1' for Rock\nType '2' for Paper\nType '3' for Scissors"))
    python = str(random.randint(1, 3))

    while player not in ["1", "2", "3"]:
        print(f"\n{player} is invalid !")
        player = str(input("\nType '1' for Rock\nType '2' for Paper\nType '3' for Scissors"))

    check(player, python)

def check(player, python):
    
    print(f"Player chose {names[player]}, Python chose {names[python]}")

    #Tie:
    if player == python:
        print("Tie !")
    #Python wins states: 
    elif python == "1" and player == "3":
        print("Python wins !")
    
    elif python == "2" and player == "1":
        print("Python wins !")
    
    elif python == "3" and player == "2":
        print("Python wins !")
    
    #if none of the above happens then that means the player wins.
    else:
        print("Player wins !")
    
    print("Press 'shift' to play again:")
    keyboard.wait('shift')
    main_menu()
    

#Code starts execuating start here: 

main_menu()