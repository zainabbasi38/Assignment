import random
DONE_LIKELIHOOD = 0.3


def chaotic_counting():
    for i in range(1,10):
        num = i + 1
        if done():
            return 
        print(num)    

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I am going to count untill 10 or fell stopping and whetever comes first")
    chaotic_counting()
    print("I am done")

main()