print("How many numbers should I sum up?")
numbers = int(input())

summed = 0

print()

total = 0
while summed < numbers:
    print(f"Please enter number {summed} of {numbers}:")
    number = int(input())
    total = total + number
    summed = summed+1

print(f"The answer is {total}.")