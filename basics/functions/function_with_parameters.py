# Beep and Bop climbing the bridge ladder

def climb_ladder(num_steps, num_crossed):
    if num_steps > num_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")
climb_ladder(5, 2)
climb_ladder(2, 5)


