print("How many rows would you like?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()

