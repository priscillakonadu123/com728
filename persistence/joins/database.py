import sqlite3

column_product = 0
column_description = 1
column_quantity = 2
column_supplier = 1

def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, description, quantity " \
          "FROM product " \
          "NATURAL JOIN stock"

    cursor.execute(sql)
    records = cursor.fetchall()


    print(f"There are {len(records)} products in the catalogue.")
    print("The stock level for each product is as follows:")

    for record in records:
        print(f"Product: {record[column_product]}")
        print(f"Description: {record[column_description]}")
        print(f"Stock level: {record[column_quantity]}")
        print()
    db.commit()
    db.close()


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.product_name, supplier.supplier_name " \
          "FROM product INNER JOIN supplier " \
          "ON product.supplier_id = supplier.id"

    cursor.execute(sql)
    records = cursor.fetchall()


    print("The suppliers for each product are as follows:")

    for record in records:
        print(f"Product: {record[column_product]}, Supplier: {record[column_supplier]}")

    db.commit()
    db.close()