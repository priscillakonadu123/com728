import csv

def extract(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        names=""

        print("Values:")
        for values in csv_reader:
            print(values[1])

extract("bots.csv")