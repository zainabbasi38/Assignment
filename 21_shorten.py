MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def get_ist():
    list = []
    elem = input("Enter an element in a list or press enter to stop. ")
    while elem != "":
        list.append(elem)
        elem = input("Enter an element in a list or press enter to stop. ")

    return list

def main():
    ist = get_ist()
    shorten(ist)


if __name__=="__main__":
    main()