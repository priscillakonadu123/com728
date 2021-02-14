print("Please enter the cover type (hard or soft)")
cover_type = input()

if cover_type == "soft":
    print("Is the book perfectly bound?")
    perfectly_bound = input()
    if perfectly_bound == "yes":
        print("Soft cover, perfect-bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")



