class StudentRecordManager:
    def __init__(self):
        self.records = []  # List to hold student records
        self.filename = None

    def open_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.records = [tuple(record.values()) for record in data]  # Convert dict to tuple
                self.filename = filename
                print(f"File '{filename}' opened successfully.")
        except Exception as e:
            print(f"Error opening file: {e}")

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                data = [{'student_id': record[0], 'name': record[1:], 'class_standing': record[3], 'major_exam_grade': record[4]} for record in self.records]
                json.dump(data, file)
                print(f"Records saved to '{self.filename}'.")
        else:
            print("No file is currently open. Use 'Save As' to save the records.")

    def save_as_file(self, filename):
        self.filename = filename
        self.save_file()

    def show_all_records(self):
        if not self.records:
            print("No records available.")
            return
        for record in self.records:
            print(record)

    def order_by_last_name(self):
        self.records.sort(key=lambda x: x[1][1])  # Sort by last name
        print("Records ordered by last name.")

    def order_by_grade(self):
        self.records.sort(key=lambda x: 0.6 * x[3] + 0.4 * x[4], reverse=True)  # Sort by calculated grade
        print("Records ordered by grade.")

    def show_student_record(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                print(record)
                return
        print("Student record not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam_grade):
        if any(record[0] == student_id for record in self.records):
            print("Record with this Student ID already exists.")
            return
        new_record = (student_id, (first_name, last_name), class_standing, major_exam_grade)
        self.records.append(new_record)  # Add new record to the list
        print("Record added successfully.")

    def edit_record(self, student_id, first_name=None, last_name=None, class_standing=None, major_exam_grade=None):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                name = list(record[1])  # Convert tuple to list to modify
                if first_name:
                    name[0] = first_name
                if last_name:
                    name[1] = last_name
                if class_standing is not None:
                    record = (record[0], tuple(name), class_standing, record[3])
                if major_exam_grade is not None:
                    record = (record[0], tuple(name), record[2], major_exam_grade)
                self.records[i] = record  # Update the record
                print("Record updated successfully.")
                return
        print("Student record not found.")

    def delete_record(self, student_id):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                del self.records[i]  # Remove record from the list
                print("Record deleted successfully.")
                return
        print("Student record not found.")


def main():
    manager = StudentRecordManager()
    
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            filename = input("Enter filename to open: ")
            manager.open_file(filename)
        elif choice == '2':
            manager.save_file()
        elif choice == '3':
            filename = input("Enter filename to save as: ")
            manager.save_as_file(filename)
        elif choice == '4':
            manager.show_all_records()
        elif choice == '5':
            manager.order_by_last_name()
        elif choice == '6':
            manager.order_by_grade()
        elif choice == '7':
            student_id = input("Enter Student ID: ")
            manager.show_student_record(student_id)
        elif choice == '8':
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam_grade = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, major_exam_grade)
        elif choice == '9':
            student_id = input("Enter Student ID to edit: ")
            first_name = input("Enter new First Name (leave blank to keep unchanged): ") or None
            last_name = input("Enter new Last Name (leave blank to keep unchanged): ") or None
            class_standing = input("Enter new Class Standing Grade (leave blank to keep unchanged): ")
            class_standing = float(class_standing) if class_standing else None
            major_exam_grade = input("Enter new Major Exam Grade (leave blank to keep unchanged): ")
            major_exam_grade = float(major_exam_grade) if major_exam_grade else None
            manager.edit_record(student_id, first_name, last_name, class_standing, major_exam_grade)
        elif choice == '10':
            student_id = input("Enter Student ID to delete: ")
            manager.delete_record(student_id)
        elif choice == '11':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()