def string_manipulations():
    
    first_name = input("Enter your first name: ")  
    last_name = input("Enter your last name: ")    
    age = input("Enter your age: ")                  

    # Concatenate first name and last name
    full_name = first_name + " " + last_name  
    print(f"\nFull Name: {full_name}")  # Display full name

    # Slice the first three characters of the first name
    sliced_name = first_name[0:3]  
    print(f"Sliced Name: {sliced_name}")  # Display sliced name

    # Create a greeting message using string formatting
    greeting_message = "Hello, {}! Welcome. You are {} years old.".format(sliced_name, age)  
    print(f"Greeting Message: {greeting_message}")  # Display greeting message

# Call the function
string_manipulations()