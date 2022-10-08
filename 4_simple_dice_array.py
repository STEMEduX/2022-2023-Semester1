##
## simple_dice.py

import random

def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled
  
def main():
    sides = 24

    sides = input("How faces of die do you want to roll? ")

    if sides.isnumeric():
        sides = int(sides)
    else:
        sides = 6

    a = [0] * sides
    totalrolls = 0

    totalrolls = input("How many times do you want to roll? ")

    if totalrolls.isnumeric():
        for i in range(0, int(totalrolls)):
        
            num_rolled = roll(sides)
            print("You rolled a ", num_rolled)

            a[num_rolled - 1] = a[num_rolled - 1] + 1

        print("Thanks for playing.")
        print("Total rolls", totalrolls);

        for j in range(0, int(sides)):
            print("number", j + 1, "showed up", a[j], "probability", a[j]/int(totalrolls));
        
    else:
        print("You should enter a number for playing. Please start over")

main()
