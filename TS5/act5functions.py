def mathematical_operations():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting the program.")
            break
        
        if choice == 'D':
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {result}")

        elif choice == 'E':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = base ** exponent
            print(f"Result: {result}")

        elif choice == 'R':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 % num2
                print(f"Result: {result}")

        elif choice == 'F':
            start = int(input("Enter the first number (start): "))
            end = int(input("Enter the second number (end): "))
            if start >= end:
                print("Error: The second number must be greater than the first number.")
            else:
                result = sum(range(start, end + 1))
                print(f"Result: {result}")

        else:
            print("Invalid choice. Please try again.")

# Call the function
mathematical_operations()