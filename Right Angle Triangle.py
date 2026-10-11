print("Half Pyramid Pattern of Stars(*):")
n = int(input("Enter number of rows:"))
#outer loop to handle number of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i + 1):
        print("*", end="")
    print()