def search(file_path):
    print("Searching...")

    sections = ""
    books = "books:\n"


    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")

    return f"{sections}\n\n{books}"

def save (file_path,data):
    print("Saving...")
    with open(file_path,"w") as file:
        file.write(data):
    print("Done!")

def run():
    data = search("books.txt")
    save("books.txt", data)
