def search(file_path):
    print("Searching...")
    with open(file_path) in file:
         for line in file:
             print(f"Looked in {line}")
    print("Done!")


def run():
    search("library.txt")

run()