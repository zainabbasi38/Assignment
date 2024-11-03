PETURSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    Age = int(input("How old are you? "))

    if Age>=PETURSBOUIPO_AGE:
        print(f"You can vote in petursbouipo where the voting age is {PETURSBOUIPO_AGE}")
    else:
        print(f"You can't vote in petursbouipo where the voting age is {PETURSBOUIPO_AGE}")

    if Age>=STANLAU_AGE:
        print(f"You can vote in stanlau where the voting  age is {STANLAU_AGE}")
    else:
        print(f"You can't vote in stanlau where the voting  age is {STANLAU_AGE}")

    if Age>=MAYENGUA_AGE:
        print(f"You can vote in mayengua where the voting age is {MAYENGUA_AGE}")
    else:
        print(f"You can't vote in mayengua where the voting age is {MAYENGUA_AGE}")

main()