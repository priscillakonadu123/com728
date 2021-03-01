def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for line in file:
            print(f"Looked in {file}")

    print("...Done!")

def run():
    search("library.txt")

run()