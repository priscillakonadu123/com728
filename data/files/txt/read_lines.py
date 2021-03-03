
def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            print(f"Looked in {line}")

    print("...Done!")

def run():
    search("library.txt")

run()