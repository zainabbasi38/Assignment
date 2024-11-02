def get_last_element(Ist):

    print(Ist[-1])

def get_Ist():
    Ist = []
    elem = input("Enter an element in a list or press enter to stop: ")
    while elem != "":
        Ist.append(elem)
        elem = input("Enter an element in a list or press enter to stop: ")
    return Ist

def main():
    Ist = get_Ist()
    get_last_element(Ist)

main()
