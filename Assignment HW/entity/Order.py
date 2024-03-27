from datetime import datetime

class Order:
    def __init__(self, order_id, customer, products=None):
        self.order_id = order_id
        self.customer = customer
        self.order_date = datetime.now()
        self.products = products if products else []

    def calculate_total_amount(self):
        return sum(product.price for product in self.products)

    def get_order_details(self):
        order_details = f"Order ID: {self.order_id}\nCustomer: {self.customer.first_name} {self.customer.last_name}\nOrder Date: {self.order_date}\nTotal Amount: ${self.calculate_total_amount()}\n"
        for product in self.products:
            order_details += f"\n{product.get_product_details()}"
        return order_details

    def update_order_status(self, status):
        # Code to update order status
        pass

    def cancel_order(self):
        # Code to cancel order
        pass

    @property
    def OrderID(self):
        return self.__OrderID

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, customer):
        # Add validation logic if needed
        self.__Customer = customer

    @property
    def OrderDate(self):
        return self.__OrderDate

    @OrderDate.setter
    def OrderDate(self, order_date):
        if isinstance(order_date, datetime):
            self.__OrderDate = order_date
        else:
            raise ValueError("Order date must be a datetime object.")

    @property
    def TotalAmount(self):
        return self.__TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, total_amount):
        if isinstance(total_amount, (int, float)):
            self.__TotalAmount = total_amount
        else:
            raise ValueError("Total amount must be a numeric value.")