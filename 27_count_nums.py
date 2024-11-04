def get_user_numbers():

    List = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
        
        num = int(user_input)
        List.append(num)
    
    return List

def count_nums(num_lst):

    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):

    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():

    user = get_user_numbers()
    num_dict = count_nums(user)
    print_counts(num_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()
