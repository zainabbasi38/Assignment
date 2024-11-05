AFFIRMATION = "I am capable to do anything and i put main to"

def main():
    print("Please type the following affirmation: " + str(AFFIRMATION))
    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("That's was not the affirmation")

        print()
        print("Please enter correct affirmation")
        user_feedback = input()

    print("Congrats!, that's right")

if __name__== "__main__":
    main()
