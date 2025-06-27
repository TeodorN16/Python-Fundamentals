while True:
    try:
        first_number = int(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = int(input("Enter the second number: "))

        if operator == "+":
            print(f"Result: {first_number + second_number}")
        elif operator == "-":
            print(f"Result: {first_number - second_number}")
        elif operator == "*":
            print(f"Result: {first_number * second_number}")
        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {first_number / second_number}")
        else:
            print("Invalid operator.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Calculator closed.")
        break
