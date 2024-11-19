import logging

logging.basicConfig(filename='inventory.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Item:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_stock(self, quantity):
        self.quantity += quantity
        self.log_stock_change(quantity)

    def log_stock_change(self, quantity):
        logging.info(f"Updated {self.name}: {quantity} units. New Quantity: {self.quantity}")

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

class PhysicalItem(Item):
    def __init__(self, id, name, quantity, price, weight, dimensions):
        super().__init__(id, name, quantity, price)
        self.weight = weight
        self.dimensions = dimensions

    def get_info(self):
        return super().get_info() + f", Weight: {self.weight}, Dimensions: {self.dimensions}"

class DigitalItem(Item):
    def __init__(self, id, name, quantity, price, file_size, download_link):
        super().__init__(id, name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def get_info(self):
        return super().get_info() + f", File Size: {self.file_size}, Download Link: {self.download_link}"