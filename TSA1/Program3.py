
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()




i = 1
while i <= 5:
    j = 1
    while j <= i*2 - 1:
        print(i, end="")
        j += 1
    print()
    i += 1