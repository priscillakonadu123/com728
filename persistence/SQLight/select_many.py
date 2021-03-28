import sqlite3

def retrieve_bots():
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()
    sql = "SELECT * FROM bots;"

    cursor.execute(sql)

    single_row = cursor.fetchone()
    many_row = cursor.fetchall()

    db.close()



    print("Single bot in the system:")
    print(single_row)
    print()

    for record in many_row:
        print(record)

    db.close()

def run():
    retrieve_bots()

if __name__=="__main__":
    run()