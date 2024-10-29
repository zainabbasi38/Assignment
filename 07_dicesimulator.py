"""
program dicesimulator:

Simulate rolling two dice, three times. Prints the results of each die roll.
 This program is used to show how variable scope works.

"""
import random
Num_sides = 6
def roll_dice():
    die1 : int = random.randint(1 , Num_sides) 
    die2 : int = random.randint(1 , Num_sides)
    score = die1 + die2
    print("score of two dice: " + str(score))

def main():
    die1 :int = 10
    print("die1 in main() starts as " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() starts is " + str(die1))



if __name__ == '__main__':
    main()

