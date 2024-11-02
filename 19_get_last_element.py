"""

Problem:
Fill out the function get_last_element(lst) which takes in a list lst as a parameter
 and prints the last element in the list. The list is guaranteed to be non-empty, but 
 there are no guarantees on its length.

"""
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
