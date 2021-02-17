print("What do you what to eat today OR are you not hungry?")
food = input()
print("Let me see if i can do it for you! ...")

if (food == "pasta") or (food == "Fries") or (food == "Pizza") or (food == "burger"):
    print("yes of course. I will be right back.")

    if not (food == "pasta") or (food == "Fries") or (food == "Pizza") or (food == "burger"):
        print("Unfortunately, I have not learnt it yet.")

elif food == "I am not hungry":
    print("Oh ok. I can still prepare something for later. In case you get hungry.")

else:
    print("I am here to please your desires :)")
