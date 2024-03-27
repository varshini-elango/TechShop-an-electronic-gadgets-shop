class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.orders = []

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        return f"Customer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\nTotal Orders: {self.calculate_total_orders()}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address

    @property
    def CustomerID(self):
        return self.__CustomerID

    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, first_name):
        if isinstance(first_name, str):
            self.__FirstName = first_name
        else:
            raise ValueError("First name must be a string.")

    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, last_name):
        if isinstance(last_name, str):
            self.__LastName = last_name
        else:
            raise ValueError("Last name must be a string.")

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, email):
        # Add email validation logic here if needed
        self.__Email = email

    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, phone):
        # Add phone number validation logic here if needed
        self.__Phone = phone

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, address):
        if isinstance(address, str):
            self.__Address = address
        else:
            raise ValueError("Address must be a string.")
