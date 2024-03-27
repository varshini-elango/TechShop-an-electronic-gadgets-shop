class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def get_order_detail_info(self):
        return f"Order Detail ID: {self.order_detail_id}\nOrder ID: {self.order.order_id}\nProduct: {self.product.product_name}\nQuantity: {self.quantity}\nSubtotal: ${self.calculate_subtotal()}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def add_discount(self, discount):
        # Apply discount to the subtotal
        pass

    @property
    def OrderDetailID(self):
        return self.__OrderDetailID

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, order):
        # Add validation logic if needed
        self.__Order = order

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, product):
        # Add validation logic if needed
        self.__Product = product

    @property
    def Quantity(self):
        return self.__Quantity

    @Quantity.setter
    def Quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self.__Quantity = quantity
        else:
            raise ValueError("Quantity must be a non-negative integer.")
