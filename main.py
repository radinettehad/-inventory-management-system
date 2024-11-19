import inventorydatabase
from item import *
def display_menu():
    print("Inventory Management System")
    print("1. Add New Item")
    print("2. Update Stock")
    print("3. View All Items")
    print("4. Find Low Stock Items")
    print("5. Get Total Value of Inventory")
    print("6. Find Items by Type")
    print("7. Get Average Price of Items")
    print("8. Delete Item")
    print("9. Update Item Price")
    print("10. Retrieve Oldest Items")
    print("0. Exit")


def main():
    db = inventorydatabase.InventoryDatabase('inventorydatabase', 'radin', 'Admin@4763')

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_type = input("Enter item type (Physical/Digital): ")
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            if item_type.lower() == 'physical':
                weight = float(input("Enter weight: "))
                dimensions = input("Enter dimensions: ")
                item = PhysicalItem(None, name, quantity, price, weight, dimensions)
            elif item_type.lower() == 'digital':
                file_size = float(input("Enter file size: "))
                download_link = input("Enter download link: ")
                item = DigitalItem(None, name, quantity, price, file_size, download_link)
            else:
                print("Invalid item type.")
                continue

            db.insert_item(item)
            print("Item added successfully.")

        elif choice == '2':
            item_id = int(input("Enter item ID to update stock: "))
            quantity = int(input("Enter quantity to update: "))
            db.update_stock(item_id, quantity)
            print("Stock updated successfully.")

        elif choice == '3':
            items = db.retrieve_all_items()
            for item in items:
                print(item)

        elif choice == '4':
            threshold = int(input("Enter stock threshold: "))
            low_stock_items = db.find_low_stock_items(threshold)
            for item in low_stock_items:
                print(item)

        elif choice == '5':
            total_value = db.total_value()
            print(f"Total value of inventory: {total_value}")

        elif choice == '6':
            item_type = input("Enter item type (Physical/Digital): ")
            items = db.find_items_by_type(item_type)
            for item in items:
                print(item)

        elif choice == '7':
            average_price = db.average_price()
            print(f"Average price of items: {average_price}")

        elif choice == '8':
            item_id = int(input("Enter item ID to delete: "))
            db.delete_item(item_id)
            print("Item deleted successfully.")

        elif choice == '9':
            item_id = int(input("Enter item ID to update price: "))
            new_price = float(input("Enter new price: "))
            db.update_price(item_id, new_price)
            print("Price updated successfully.")

        elif choice == '10':
            oldest_items = db.retrieve_oldest_items()
            for item in oldest_items:
                print(item)

        elif choice == '0':
            db.close()
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()