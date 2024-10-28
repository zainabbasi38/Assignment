def main():
    degrees_fahrenheit = float(input("Enter fahrenheit temperature: "))
    degrees_celcius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celcius}°C")
    print()

main()

if __name__ == "__main__":
    main()