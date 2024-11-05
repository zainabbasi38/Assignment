MAX_TERM_VALUE = 10000

def main():
    curr_value = 0
    next_value = 1
    while curr_value <= MAX_TERM_VALUE:
        print(curr_value)
        next_after_value = curr_value + next_value
        curr_value = next_value
        next_value = next_after_value
if __name__=="__main__":
    main()