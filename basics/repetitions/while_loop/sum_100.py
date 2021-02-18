print("Calculating the sum of the first 100 numbers...")

# declare a control variable
number = 1
# calculate sum of first 100 numbers
total = 0

while number <= 100:
    total = total + number
    number = number + 1

    print (f"...Done! The answer is {total}")