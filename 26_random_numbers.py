
import random

MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    Ist = []
    for number in range(1,11):
        number = random.randint(MIN_VALUE,MAX_VALUE)
        Ist.append(number)
    print(Ist)
    pass
if __name__ == '__main__':
    main()