"""
Problem:

Simulate rolling two dice, and prints results of each roll as well as the total.
"""

import random

Num_sides : int = 6

def main():
    die1 :int = random.randint(1,Num_sides)
    die2 :int = random.randint(1,Num_sides)

    total : int = die1 + die2

    print("Each dice has "+ str(Num_sides)+ " sides")

    print("Die1 score: "+ str(die1))
    print("Die2 scor:e "+ str(die2))

    print(f"Total score of two dice: {total}")

if __name__ =="__main__":
    main()

