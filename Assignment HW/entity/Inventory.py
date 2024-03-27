from datetime import datetime

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update=None):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update if last_stock_update else datetime.now()
    
    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
        self.last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
        else:
            print("Insufficient quantity in stock.")

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity
        self.last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock

    def list_low_stock_products(self, threshold):
        if self.quantity_in_stock < threshold:
            return self.product

    def list_out_of_stock_products(self):
        if self.quantity_in_stock == 0:
            return self.product

    def list_all_products(self):
        return self.product
    @property
    def InventoryID(self):
        return self.__InventoryID

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, product):
        # Add validation logic if needed
        self.__Product = product

    @property
    def QuantityInStock(self):
        return self.__QuantityInStock

    @QuantityInStock.setter
    def QuantityInStock(self, quantity_in_stock):
        if isinstance(quantity_in_stock, int) and quantity_in_stock >= 0:
            self.__QuantityInStock = quantity_in_stock
        else:
            raise ValueError("Quantity in stock must be a non-negative integer.")

    @property
    def LastStockUpdate(self):
        return self.__LastStockUpdate

    @LastStockUpdate.setter
    def LastStockUpdate(self, last_stock_update):
        if isinstance(last_stock_update, datetime):
            self.__LastStockUpdate = last_stock_update
        else:
            raise ValueError("Last stock update must be a datetime object.")