import sqlite3

def get_bot_id_from_user():
    print("Please enter a bot id:")
    id = int(input())

    return id

def display_bot_from_db(id):
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()

    sql = f"SELECT * FROM bots WHERE id = {id}"
    cursor.execute(sql)
    single_row = cursor.fetchall()
    db.close()

    print(single_row)

def get_bot_details_from_user():
    print("Please enter the name of field to be updated and enter the new value for the"
          "field")
    field = input()
    value = int(input())

    if field =="speed":
        value = input()

    return field, value

def update_bot_in_db(data):
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()

    sql = f"UPDATE bots SET {data[0]}={data[1]}"
    cursor.execute(sql)

    db.commit""
    db.close()
    print("Updated.")

def run():

    id = get_bot_id_from_user()
    display_bot_from_db(id)

    data = get_bot_details_from_user()
    update_bot_in_db(data)

if __name__=="__main__":
    run()







