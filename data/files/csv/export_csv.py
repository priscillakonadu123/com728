import csv

def export(file_path, integer):
    print("Exporting...")
    with open("exported_bots.csv", "a") as file:
        for bot in file:
            bot_id = int(input())
            bot_name = input()
            bot_paint = input()

            csv = f"{bot_id},{bot_name},{bot_paint}"

            print("Done!")

def run():
    export("exported_bots.csv", 0)

