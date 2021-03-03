def writing(file_path):
    print("Exporting...")
    with open(file_path, "w") as file:

        # lines = file.readlines()
        # for line in lines:
        # print(f"{lines}")

        print("Please enter the bot id:")
        bot_id = int(input())

        print("Please enter the bot name:")
        bot_name = input()

        print("Please enter the bot paint:")
        bot_paint = input()

        value = f"\n{bot_id},{bot_name},{bot_paint}"
        file.write(value)

def run():
    writing("writing.csv")

run()


