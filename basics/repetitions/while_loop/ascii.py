print("How many bars should be charged?")
bars_to_be_charged = int(input())

numbers_bars_charged = 0

print()

while numbers_bars_charged < bars_to_be_charged:
    numbers_bars_charged += 1
    print(f"Charging: {'█'* numbers_bars_charged}")

    print("The battery is fully charged.")