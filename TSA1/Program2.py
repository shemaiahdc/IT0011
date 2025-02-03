def sum_of_digits(string):
    sum = 0
    for char in string:
        if char.isdigit():
            sum += int(char)
    return sum

input_string = input("Enter a string with digits: ")
sum = sum_of_digits(