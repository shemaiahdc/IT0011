def read_student_info():
    try:
        
        with open("students.txt", "r") as file:
            print("Reading Student Information:")
            print("------------------------------")
            
            
            contents = file.readlines()  
            
            
            for line in contents:
                print(line.strip())  
    
    except FileNotFoundError:
        print("Error: The file 'students.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_student_info()