##
## simple_dice.py

import random


def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled
  
def main():
    sides = 6
    rolling = True
    numberone = 0
    numbertwo = 0
    numberthree = 0
    numberfour = 0
    numberfive = 0
    numbersix = 0
    totalrolls = 0

    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
        
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a ", num_rolled)

            totalrolls = totalrolls + 1

            if num_rolled == 1:
                numberone = numberone + 1
            if num_rolled == 2:
                numbertwo = numbertwo + 1
            if num_rolled == 3:
                numberthree = numberthree + 1
            if num_rolled == 4:
                numberfour = numberfour + 1
            if num_rolled == 5:
                numberfive = numberfive + 1
            if num_rolled == 6:
                numbersix = numbersix + 1  
        else:
            rolling = False

    print("Thanks for playing.")
    print("Total rolls", totalrolls);
    print("number 1 showed up", numberone, "probability", numberone/totalrolls);
    print("number 2 showed up", numbertwo, "probability", numbertwo/totalrolls);
    print("number 3 showed up", numberthree, "probability", numberthree/totalrolls);
    print("number 4 showed up", numberfour, "probability", numberfour/totalrolls);
    print("number 5 showed up", numberfive, "probability", numberfive/totalrolls);
    print("number 6 showed up", numbersix, "probability", numbersix/totalrolls)

main()