history = []

while True:
    print("\n1. Convert Celsius to Fahrenheit.")
    print("2. Convert Fahrenheit to Celsius.")
    print("3. View conversion history.")
    print("4. Exit")

    action = int(input("Choose an option: "))

    if action == 1:
        degrees = int(input("Enter degrees in Celsius: "))
        fahrenheit = (degrees * 9) / 5 + 32
        history.append({
            "Celsius": f"{degrees}°C",
            "Fahrenheit": f"{fahrenheit:.2f}°F"
        })
        print(f"Result: {degrees}°C = {fahrenheit:.2f}°F")

    elif action == 2:
        degrees = int(input("Enter degrees in Fahrenheit: "))
        celsius = (degrees - 32) * 5 / 9
        history.append({
            "Fahrenheit": f"{degrees}°F",
            "Celsius": f"{celsius:.2f}°C"
        })
        print(f"Result: {degrees}°F = {celsius:.2f}°C")

    elif action == 3:
        if not history:
            print("No conversions yet.")
        else:
            print("\n--- Conversion History ---")
            for index, item in enumerate(history, 1):
                print(f"{index}. ", end="")
                print(" | ".join(f"{key}: {value}" for key, value in item.items()))

    elif action == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 4.")

    goagain = input("\nContinue? (y/n): ").strip().lower()
    if goagain != "y":
        print("Goodbye!")
        break
