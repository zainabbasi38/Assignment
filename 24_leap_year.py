def main():
    year :int = int(input("Please input a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year")
            else:
                print("That's not a leap year")
        else:
            print("That's a leap year")
    else:
        print("That's not a leap year")

main()