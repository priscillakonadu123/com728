import sqlite3

column_product = 0
column_description = 1
column_quantity = 2
column_supplier = 1
column_location = 3


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


def display_product_supplier_locations():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.product_name, supplier.supplier_name, location.city, location.country " \
          "FROM product INNER JOIN supplier " \
          "ON product.supplier_id = supplier.id " \
          "INNER JOIN location ON supplier.location_id = location.id;"

    cursor.execute(sql)
    records = cursor.fetchall()

    print("The suppliers for each product are as follows:")

    for record in records:
        print(
            f"Product: {record[column_product]}, Supplier: {record[column_supplier]}, Supplier Location: {record[column_location]}")

    db.commit()
    db.close()


def display_products_missing_suppliers():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.product_name, supplier.supplier_name, location.city, location.country " \
          "FROM product LEFT OUTER JOIN supplier " \
          "ON product.supplier_id = supplier.id " \
          "LEFT OUTER JOIN location ON supplier.location_id = location.id;"

    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(
            f"Product: {record[column_product]}, Supplier: {record[column_supplier]}, Supplier Location: {record[column_location]}")
    db.commit()
    db.close()


def display_suppliers_missing_products():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product_name, supplier_name FROM supplier LEFT OUTER JOIN product ON supplier.id = product_id"

    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"Supplier: {record[1]}, Product: {record[0]}")

    db.commit()
    db.close()

def display_missing_data():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product_name, supplier_name " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier_id"

    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        if records[0] == None:

            print("The following products are missing suppliers:")
            print(f"{record[1]}")

            print("The following suppliers are missing products:")
            print(f"{record[0]}")

            print("The following locations are not associated with a supplier:")
            print(f"{record[3]}")

    db.commit()
    db.close()