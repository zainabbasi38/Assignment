"""

Problem:
Write a program which continuously asks the user to enter values which are added one by one into a list.
 When the user presses enter without typing anything, print the list

"""
def main():
    list = []

    user_input = input("Enter an element to add on a list: ")
    while user_input:
        list.append(user_input)
        user_input = input("Enter an element to add in list: ")

    print("Here is the list: " + str(list))
if __name__== "__main__":
    main()