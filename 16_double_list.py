"""
Problem:
Write a program that doubles each element in a list of numbers. 
For example, if you start with this list:

"""

def main():
    numbers :list[int] = [1,3,5,8]

    for i in range(len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2

    print(f"Numbers {numbers}")

if __name__ == "__main__":
    main()