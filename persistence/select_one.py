import sqlite3



def retrieve_bot():
    db = sqlite3.connect("Database.db")
    cursor = db.cursor()
    sql = "SELECT * FROM bots WHERE id=1"

    cursor.execute(sql)

#fetch one, all, many with size
    single_row = cursor.fetchall()
    #record[] records say th 1st or 2nd record in thw list
    print(single_row)

    db.close()

    print(single_row)

def run():
    retrieve_bot()

if __name__=="__main__":
    run()