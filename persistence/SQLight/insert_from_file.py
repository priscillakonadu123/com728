import sqlite3
import csv


def read_data_file(file_path):
    data =[]
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            data.append(line)
    return data




def insert_to_db(data):
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()
    for record in data:
        sql = "INSERT INTO bots" \
            "(name, strength, speed, created, manufacturer_id) " \
            "VALUES " \
            "(?, ?, ?, ?, ?)"
    values = [record[0], record[1], record[2], record[3], record[4]]
    cursor.execute(sql, values)
    db.commit()
    db.close()



def run():
    print("Please enter a file path:")
    file_path = input()

    bots_data = read_data_file(file_path)

    print("Inserting data into database...")
    insert_to_db(bots_data)

    print(f"Done! {len(bots_data)} records inserted.")


if __name__=="__main__":
    run()