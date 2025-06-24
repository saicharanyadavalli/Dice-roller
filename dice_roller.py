import time
import os
from random import randint

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dicerollanimation(finalnumber):
    numbers = ['1', '2', '3', '4', '5', '6']
    
    for _ in range(2):
        for number in numbers:
            clearscreen()
            print("\n Rolling the dice...\n")
            print(f"       {number}")
            time.sleep(0.1)

    clearscreen()
    print("\n🎲 Final roll...\n")
    print(f"       {finalnumber}")
    print("\nYou rolled a", finalnumber)

input("Press Enter to roll the dice...")
final = randint(1, 6)
dicerollanimation(str(final))

