import psycopg2
from item import *

class InventoryDatabase:
    def __init__(self, db_name, user, password, host='localhost', port='5432'):
        self.connection = psycopg2.connect(database='inventorydatabase', user='radin', password='Admin@4763', host=host, port=port)
        self.cursor = self.connection.cursor()

    def insert_item(self, item):
        if isinstance(item, PhysicalItem):
            self.cursor.execute("INSERT INTO inventory (name, quantity, price, type, weight, dimensions) VALUES (%s, %s, %s, %s, %s, %s)",
                                (item.name, item.quantity, item.price, 'Physical', item.weight, item.dimensions))
        elif isinstance(item, DigitalItem):
            self.cursor.execute("INSERT INTO inventory (name, quantity, price, type, file_size, download_link) VALUES (%s, %s, %s, %s, %s, %s)",
                                (item.name, item.quantity, item.price, 'Digital', item.file_size, item.download_link))
        self.connection.commit()

    def update_stock(self, item_id, quantity):
        self.cursor.execute("UPDATE inventory SET quantity = quantity + %s WHERE id = %s", (quantity, item_id))
        self.connection.commit()

    def retrieve_all_items(self):
        self.cursor.execute("SELECT * FROM inventory")
        return self.cursor.fetchall()

    def find_low_stock_items(self, threshold):
        self.cursor.execute("SELECT * FROM inventory WHERE quantity < %s", (threshold,))
        return self.cursor.fetchall()

    def total_value(self):
        self.cursor.execute("SELECT SUM(price * quantity) FROM inventory")
        return self.cursor.fetchone()[0]

    def find_items_by_type(self, item_type):
        self.cursor.execute("SELECT * FROM inventory WHERE type = %s", (item_type,))
        return self.cursor.fetchall()

    def average_price(self):
        self.cursor.execute("SELECT AVG(price) FROM inventory")
        return self.cursor.fetchone()[0]

    def delete_item(self, item_id):
        self.cursor.execute("DELETE FROM inventory WHERE id = %s", (item_id,))
        self.connection.commit()

    def update_price(self, item_id, new_price):
        self.cursor.execute("UPDATE inventory SET price = %s WHERE id = %s", (new_price, item_id))
        self.connection.commit()

    def retrieve_oldest_items(self):
        self.cursor.execute("SELECT * FROM inventory ORDER BY date_added ASC")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()