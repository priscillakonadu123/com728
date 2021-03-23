import sqlite3

def get_bot_from_user():

    print("Please enter the name for a single bot?")
    name = input()
    print("Please enter the max strength for a single bot?")
    strength = int(input())
    print("Please enter the max speed for a single bot?")
    speed = int(input())
    print("Please enter the date for a single bot?")
    created = input()
    print("Please enter the manufacturer for a single bot?")
    manufacturer_id = int(input())

    return [name, strength, speed, created, manufacturer_id]

def insert_bot_in_db(data):

    db = sqlite3.connect("Database.db")
    cursor = db.cursor()
    sql = "INSERT INTO bots" \
          "(name, strength, speed, created, manufacturer_id) " \
          "VALUES " \
          f"('{data[0]}',{data[1]}, {data[2]}, '{data[3]}', {data[4]});"

    db.commit()
    cursor.execute(sql)

    row_id = cursor.lastrowid
    db.close()
    print(f"ID of new record is {row_id}")

def run():
    data = get_bot_from_user()
    insert_bot_in_db(data)

if __name__ =="__main__":
    run()

