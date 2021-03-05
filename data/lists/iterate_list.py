def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    print(directions[0:4])
    return directions

def menu():
    print("Please select a direction:")
    direction = directions()

    for index in range(len(direction)):
        print(f"{direction[index]} is at index {index}.".format(direction, index))


def run():
    menu()
if __name__=="__main__":
    run()

