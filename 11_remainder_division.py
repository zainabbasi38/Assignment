"""
Problem:
Ask the user for two numbers,
 one at a time, and then print the result of dividing the first number by the second and 
 also the remainder of the division

"""
def main():
    # get integers from user
    dividend : float = float(input("Please enter an integer to be divided: "))
    divisor :float = float(input("please enter an integer to divided by: "))
    
    quotient :float = dividend//divisor
    remainder : float = dividend % divisor

    print("the result of this division is " +str(quotient) +" and remainder is " +str(remainder))

if __name__=="__main__":
    main()