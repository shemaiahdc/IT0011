# Get the first and last term numbers from the user
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

# Check if the first term is less than or equal to the last term
if first_term > last_term:
    print("The first term must be less than or equal to the last term.")
else:
    # Initialize the sum to 0
    total_sum = 0

    # Loop through the numbers from first_term to last_term 
    for num in range(first_term, last_term + 1):
        total_sum += num

    # Display the sum of the numbers
    print(f"The sum of the numbers from {first_term} to {last_term} is {total_sum}.")