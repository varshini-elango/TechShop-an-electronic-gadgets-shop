class Product:
    def __init__(self, product_id, product_name, description, price, in_stock=True):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.in_stock = in_stock\
        
    def get_product_details(self):
        return f"Product ID: {self.product_id}\nName: {self.product_name}\nDescription: {self.description}\nPrice: ${self.price}\nIn Stock: {'Yes' if self.in_stock else 'No'}"

    def update_product_info(self, price=None, description=None, in_stock=None):
        if price:
            self.price = price
        if description:
            self.description = description
        if in_stock is not None:
            self.in_stock = in_stock

    def is_product_in_stock(self):
        return self.in_stock
    
    @property
    def ProductID(self):
        return self.__ProductID

    @property
    def ProductName(self):
        return self.__ProductName

    @ProductName.setter
    def ProductName(self, product_name):
        if isinstance(product_name, str):
            self.__ProductName = product_name
        else:
            raise ValueError("Product name must be a string.")

    @property
    def Description(self):
        return self.__Description

    @Description.setter
    def Description(self, description):
        if isinstance(description, str):
            self.__Description = description
        else:
            raise ValueError("Description must be a string.")

    @property
    def Price(self):
        return self.__Price

    @Price.setter
    def Price(self, price):
        if isinstance(price, (int, float)):
            self.__Price = price
        else:
            raise ValueError("Price must be a numeric value.")