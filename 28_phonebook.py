"""
Problem:
In this program we show an example of using dictionaries to keep track 
of information in a phonebook.

"""

def read_phone_numbers():
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> "+ str(phonebook[name]))

def lockup(phonebook):
    while True:
       name = input("Enter name to lockup: ")

       if name == "":
            break
       if name not in phonebook:
            print(name + "not in the phonebook")

       else:
            print(phonebook[name])
    
def main():
    book = read_phone_numbers()
    print_phonebook(book)
    lockup(book)

if __name__=="__main__":
    main()