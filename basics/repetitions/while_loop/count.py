print("How many live cables must I avoid?")
avoid_cables = int(input())

live_cables = 0

while live_cables < avoid_cables:
    print("Avoiding...", end="") # <--- means nothing comes after the print and starts in the next line
    live_cables += 1
    print(f" Done! {live_cables} live cable avoided!")

print("All live cables have been avoided.")

#print("the second message is", end="")
#print("on the same line")
