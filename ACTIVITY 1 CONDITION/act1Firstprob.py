# Ask the user for 3 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


order = sorted([num1, num2, num3], reverse=True)

# Display the numbers in descending order
print(f"The numbers in descending order are: {order}")