
with open('numbers.txt', 'r') as file:
    lines = file.readlines()

# Function check if palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]


for index, line in enumerate(lines):
    
    numbers = line.strip().split(',')
    
    
    int_numbers = [int(num) for num in numbers]
    
    
    total_sum = sum(int_numbers)
    
    
    palindrome_status = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
    
    # Display the result
    print(f"Line {index + 1}: {','.join(numbers)} (sum {total_sum}) - {palindrome_status}")