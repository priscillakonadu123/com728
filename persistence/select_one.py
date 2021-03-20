import sqlite3



def retrieve_bot():
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()
    sql = "SELECT * FROM bots"

    cursor.execute(sql)

    single_row = cursor.fetchall()
    print(single_row)

    db.close()

    print(single_row)

def run():
    retrieve_bot()

if __name__=="__main__":
    run()