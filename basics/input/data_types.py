# Create Data types

name = input("What is your name human?")
user_age = int(input("What is your age"))
weight = int(input("What is your weight"))
height = float(input("What is your height"))

# calculate bmi
bmi = weight /(height ** 2)

# Display results
print(f" {name}, you are {user_age} years old and your bmi is {bmi}")