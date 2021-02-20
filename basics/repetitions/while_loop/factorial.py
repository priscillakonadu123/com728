# 1 x 2 x 3 x 4

print("Please enter a number:")
number = int(input())


count = 0
factorial = 1

while count < number:
    print(f"factorial:{factorial}", f"count:{count}")
    count += 1
    factorial = factorial * count

print(f"The factorial is {factorial}.")
# factorial=1 count=1
# factorial=1 count=2
# factorial=2 count=3
# factorial=6 count=4
# factorial=24 count=5

