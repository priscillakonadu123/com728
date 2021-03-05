# Beep and Bop are escsping the cave

def directions():
    direction =["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    print(direction[0:4])
    return direction
def menu():
    print("Please select a direction:")
    path =directions()

    for index in range(len(path)):
        print("{}:{}".format(index, path[index]))
    response = str(int(input()))
    return path[index]
def run():
    route=[]
    print("Working out escape route...")

    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


run()
