print("Calculating the sum of the first 100 numbers...")

# declare a control variable
number = 1
# calculate sum of first 100 numbers
total = 0

print("number", "total")

while number <= 100:
    total = total + number
    print(number, total)
    number += 1

print(f"...Done! The answer is {total}")