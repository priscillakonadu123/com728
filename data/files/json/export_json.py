import json

def read(file_path):
    print("Reading...", end="")

    with open(file_path, "r") as file:
        data=json.load(file)
        print("Done!")
        return data

def save(file_path, data_saved):
    print("Exporting..", end="")
    data_saved = {
  "name": "Beep",
  "type": "Bot"
}

    with open("exported.json", "w") as file:
        json.dump(data_saved, file, indent = 4)

    print("Done!")

def run():
    json_data=read("robocity.json")
    save("export_json.py", json_data)

if __name__ == "__main__":
    run()


