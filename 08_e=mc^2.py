C : int = 299792458

def main():
    mass_in_kg : float = float(input("Enter mass in kilogram: "))
    energy_in_joules = mass_in_kg * C ** 2
    print("e = m*c**2")
    print("mass " + str(mass_in_kg) + "kg")
    print("Energy in joules: " + str(energy_in_joules) + " Jolues")

if __name__ == "__main__":
    main()