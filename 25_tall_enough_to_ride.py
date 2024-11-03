MAXIMUM_HEIGHT : int = 72
MINIMUM_HEIGHT : int = 60

def main():
    height : float = float(input("How tall are you? "))
    if height <= MAXIMUM_HEIGHT and height >=MINIMUM_HEIGHT:
        print("you can take the ride")
    else:
        print("You can't take ride but may be next year")
if __name__=="__main__":
    main()