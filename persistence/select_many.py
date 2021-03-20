import sqlite3

def retrieve_bots():
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()
    sql = "SELECT * FROM bots WHERE id=1"

    cursor.execute(sql)

    single_row = cursor.fetchone()
    many_row = cursor.fetchall()

    print("Single bot in the system:")
    print(single_row)
    print("All bots in the system:")
    print(many_row)

    db.close()
def run():
    retrieve_bots()

if __name__=="__main__":
    run()