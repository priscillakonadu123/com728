print("What level of brightness is required?")
brightness_level = int(input())


print("\n Adjusting brightness..\n")

for brightness in range(2,brightness_level+1, 2):
    print(f"Beeps's brightness level:{'*' * brightness}")
    print(f"Bop's brightness level:{'*' * brightness}")

print("Adjustments complete!")

