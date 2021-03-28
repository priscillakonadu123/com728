
import database as data



def menu():
    print("Please select one of the following options:")
    print()
    print("""
    [1] Display stock levels
    [2] Display suppliers
    """)

    print("Your selection:")
    selection = int(input())

    return selection



def run():
    selection = menu()
    if selection == 1:
        print(data.display_products_with_stock_levels())
    elif selection == 2:
        print(data.display_product_supplier())
    else:
        print("invaled selection!")


if __name__ =="__main__":
    run()