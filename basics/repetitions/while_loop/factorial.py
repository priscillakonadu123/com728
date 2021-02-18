# 1 x 2 x 3 x 4

print("Please enter a number:")
number = int(input())


count = 0
factorial = 1

while count < number:
    count += 1
    factorial = factorial * count

print(f"The factorial is {factorial}.")


