date_input = input("Enter the date (mm/dd/yyyy): ")


month, day, year = date_input.split('/')


month = int(month)
day = int(day)


if month < 1 or month > 12:
    print("Invalid month. Please enter a month between 1 and 12.")
else:
    
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    
    month_name = month_names[month - 1]

    
    human_readable_date = f"{month_name} {day}, {year}"

    
    print("Date Output:", human_readable_date)