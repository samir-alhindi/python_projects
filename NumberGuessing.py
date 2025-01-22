#Importing Libraries / Modules:
import random
import keyboard

#Defining the Functions:

def start_menu():
    logo()
    print("Press 'Space' to start")
    keyboard.wait('space')
    game()

def logo():
    print("\n----------------------")
    print("---Number Guessing---")
    print("----------------------\n")

def game():
    randNum = random_number_generator()
    guess = int(input("Guess the number ! (Between 1 and 20):"))

    while guess != randNum:
        if guess > randNum:
            print("Too big, Try smaller !")
        elif guess < randNum:
            print("Too small, Try bigger !")
        guess = int(input("Try another number: "))
    
    win()

def random_number_generator():
    random.seed()
    return random.randrange(1, 21)

def win():
    print("Congrats you Gussed right !!!")
    print("Press 'space' to play again: ")
    keyboard.wait('space')
    start_menu() 



#Code starts executing here:
start_menu()