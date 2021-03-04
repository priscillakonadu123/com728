import csv

def export(file_path, integer):
    print("Exporting...")
    with open(file_path, "a") as file:

        for value in range(integer):
            print("Please enter the bot id:")
            bot_id = int(input())

            print("Please enter the bot name:")
            bot_name = input()

            print("Please enter the bot paint:")
            bot_paint = input()
            value = f"\n{bot_id},{bot_name},{bot_paint}"
            file.write(value)

        print("Done!")
def run():
    export("exported_bots.csv", 3)

run()