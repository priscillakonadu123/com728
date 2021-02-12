# Create a program that allows us to help Beep learn to paint.

print("Towards which direction should I paint (up, down, left or right)?")
print_direction = input()

if print_direction == "up":
    print("I am painting in the upward direction!")
elif print_direction == "down":
    print("I am painting in the downwards direction!")
elif print_direction == "left":
    print("I am painting in the left direction!")
elif print_direction == "right":
    print("I am painting in the right direction!")
else :
    print("You have to choose a direction!")


