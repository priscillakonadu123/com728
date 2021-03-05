import json

def read(file_path):
    with open("robocity.json", "r") as file:
        data = json.load(file)
        city_name = data["city"]
        population = data["population"]


        print(f"City Name:\n{city_name}")
        print(f"Population Size:\n{population}")

        for bots in data["bots"]:
            bot_name = bots["name"]
            bot_stats = bots["stats"]

            print(f"{bot_name} has the following stats:\n{bot_stats}")

def run():
    read("robocity.json")
if __name__ == "__main__":
    run()
