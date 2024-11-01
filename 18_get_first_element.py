def get_first_element(Ist):

    print(Ist[0])

def get_list():
    Ist = []
    elem = input("Please enter an element of list and press enter to stop: ")
    while elem != "":
        Ist.append(elem)
        elem = input("plese enetr an element in list and press enter to stop: ")
    return Ist

def main():
    Ist = get_list()
    get_first_element(Ist)

if __name__=="__main__":
    main()
