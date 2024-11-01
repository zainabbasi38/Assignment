def add_three_copies(my_list,data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("Enter your message: ")
    my_list = []
    print("First list: ", my_list)
    add_three_copies(my_list,message)
    print("After list: ", my_list)

main()