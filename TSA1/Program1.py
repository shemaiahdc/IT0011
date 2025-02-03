def count_characters(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels_count = 0
    consonants_count = 0
    space_count = 0
    other_count = 0
    for char in string:
        if char in vowels:
            vowels_count += 1
        elif char in consonants:
            consonants_count += 1
        elif char == " ":
            space_count += 1
        else:
            other_count += 1

    return vowels_count, consonants_count, space_count, other_count

input_string = input("Enter a string: ")
vowels_count, consonants_count, space_count, other_count = count_characters(input_string)

print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
print("Spaces:", space_count)
print("Other characters:", other_count)