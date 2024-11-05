def main():

    import random

    secret_number = random.randint(0,99)

    print("Enter a number you are thinking")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print()
        guess = int(input(("Enetr a new guess nmber: ")))

    print("Congrats! , you guess correct number " + str(secret_number))

if __name__=="__main__":
    main()