# the built-in funktions work from the inside out
# from input to int to abs (input is naturally a string)

print("Program Started!")
print("Please enter an ASCII code:")
ascii_code = abs(int(input()))


if ascii_code in range(32, 127g):
    print(f"The character represented by the ASCII code {ascii_code} is {(chr(ascii_code))}.")
else:
    print("ERROR!")
print("Program Ended!")
