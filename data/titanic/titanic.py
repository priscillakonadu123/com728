import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)
    print("Done!")

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    else:
        print("Error! Option not recognised!.")







def display_menu():
    print( """
  Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
 

  """)

    selected_response = int(input())
    return selected_response

def display_passenger_names():
    print("The names of the passengers are....")

    for record in records:
        passenger_name = record[3]
        print(passenger_name)



if __name__ == "__main__":
    run()