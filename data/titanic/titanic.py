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

def display_bum_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0

    for record in records:
        gender = record[4]
        if gender.lower() == "male":
            males += 1
        if gender.lower() == "female":
            females += 1
    print(f"females: {females}, males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    print(f"children: {children}, adults: {adults}, elderly: {elderly}")




def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
#    else:
#        print("Error! Option not recognised!.")

    if selected_option == 2:
        display_bum_survivors()

    if selected_option == 3:
        display_passengers_per_gender()

    if selected_option == 4:
        display_passengers_per_age_group()



if __name__ == "__main__":
    run()