"""
Problem:
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle 
and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

"""

import math

def main():
# get the length of two side from the user
    side1 : float = float(input("Enter length of side AB: "))
    side2 : float = float(input("Enter length of side BC: "))

# calculate pythgorous theorem and print it out
    side3 = math.sqrt(side1**2 + side2**2)
    print("Length of side AC (the hypotinuse) is " +str(side3))

if __name__=="__main__":
    main()