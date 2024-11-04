def main():
    
    Fruits : dict = {"Apple": 2, "Banana": 2,"Grapes": 24, "Kiwi":50,"Apricot": 60}
    
    total_cost = 0
    
    for fruit in Fruits:
        price = Fruits[fruit]
        buy = int(input(f"How many {fruit} do you buy? "))
        total_cost += (price * buy)

    print(f"your total cost is {total_cost}$. ")
if __name__=="__main__":
    main()