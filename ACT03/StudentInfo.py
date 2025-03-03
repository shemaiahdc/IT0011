def save_student_info():
    # Accept input from the user
    last_name = input("Enter last name: ")  # Example of input
    first_name = input("Enter first name: ")  # Example of input
    age = input("Enter age: ")  # Example of input
    contact_number = input("Enter contact number: ")  # Example of input
    course = input("Enter course: ")  # Example of input

    # Create a formatted string containing the collected information
    student_info = (
        f"Last Name: {last_name}\n"
        f"First Name: {first_name}\n"
        f"Age: {age}\n"
        f"Contact Number: {contact_number}\n"
        f"Course: {course}\n"
    )

    try:
        # Open the file in append mode and write the formatted information
        with open("students.txt", "a") as file:  # File handling example
            file.write(student_info)  # Writing to file example

        # Display a confirmation message
        print("Student information has been saved to 'students.txt'.")
    except PermissionError:
        print("Error: Permission denied. Please check the file's permissions.")

# Call the function
save_student_info()