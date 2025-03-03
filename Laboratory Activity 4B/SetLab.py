A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

intersection_count = len(A & B)
print("Number of elements in A and B:", intersection_count)

not_in_A_or_C = B - (A | C)
not_in_A_or_C_count = len(not_in_A_or_C)
print("Number of elements in B that are not in A and C:", not_in_A_or_C_count)


# i. [h, i, j, k]
result_i = (B & C) | {'k'}
print("Result i:", result_i)

# ii. [c, d, f]
result_ii = (A & C) | {'f'}
print("Result ii:", result_ii)

# iii. [b, c, h]
result_iii = (A & B) | {'h'}
print("Result iii:", result_iii)

# iv. [d, f]
result_iv = (A & C) | {'f'}
print("Result iv:", result_iv)

# v. [c]
result_v = A & B & C
print("Result v:", result_v)

# vi. [l, m, o]
result_vi = {'l', 'm', 'o'}
print("Result vi:", result_vi)

A.add("orange")
print("Set A after adding 'orange':", A)

B.update(["kiwi", "peach"])
print("Set B after updating with ['kiwi', 'peach']:", B)

print("Length of Set A:", len(A))

B.discard("banana")  

C.clear()
print("Set C after clearing:", C)

my_dict = {
    "A": A,
    "B": B,
    "C": C
}


print("Set A from dictionary:", my_dict.get("A"))


my_dict["A"] = {"new_value"}
print("Updated dictionary:", my_dict)


for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")


print("Length of my_dict:", len(my_dict))


my_dict_copy = my_dict.copy()
print("Copied dictionary:", my_dict_copy)