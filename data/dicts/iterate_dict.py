def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences



def display_keys(data):
    print("Keys:")

    for key in data:
        print(key)
    print()

def display_values(data):
    print("Value:")

    for value in data.values():
        print(value)
    print()
def display_items(data):
    print("Pairs:")

    for key, value in data.items():
        print(key,value)
    print()

def run():
    data = pattern()

    print(f"Dictionary: \n{data}")
    display_values(data)
    display_values(data)
    display_items(data)

if __name__=="__main__":
    run()