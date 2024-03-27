class InvalidDataException(Exception):
    pass

class InsufficientStockException(Exception):
    pass

class IncompleteOrderException(Exception):
    pass

class PaymentFailedException(Exception):
    pass

class FileIOException(Exception):
    pass

class DatabaseConnectionException(Exception):
    pass

class ConcurrencyException(Exception):
    pass

class AuthenticationException(Exception):
    pass

class ProductNotAvailableException(Exception):
    pass