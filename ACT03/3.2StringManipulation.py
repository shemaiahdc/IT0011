def string_manipulations():
    
    first_name = input("Enter your first name: ")  
    last_name = input("Enter your last name: ")    

    full_name = first_name + " " + last_name  
    print(f"\nFull Name: {full_name}") 

    full_name_upper = full_name.upper()  
    print(f"Full Name (Upper Case): {full_name_upper}")  

    full_name_lower = full_name.lower()  
    print(f"Full Name (Lower Case): {full_name_lower}")  

    length_of_full_name = len(full_name)  
    print(f"Length of Full Name: {length_of_full_name}")   

string_manipulations()