print("Where should I look?")
place = input()

if place == "in the bedroom":
    print("Where in the bedroom should I look?")
    bed_place = input()

if bedroom_place == "under the bed":
    print("Found some shoes but no battery.")
else:
    print("Found some mess but no battery.")

if users_response == "in the bathroom":
    print("Where in the bathroom should I look?")