"""
Problem:
Write a program which prompts the user for an adjective, then a noun,
 then a verb, and then prints a fun sentence with those words!

"""
SENTENCE_START = "panaversity is fun.I learned a program and use pyhton to make "

def main():
    # Get three inputs from the user 
    adjective : str = input("Please enter an adjetive and press enter: ")
    noun : str = input("Please enter an noun and press enter: ")
    verb : str = input("Please enter an verb and press enter: ")
    # print out all inputs in a sentence

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "")

if __name__== "__main__": 
    main()