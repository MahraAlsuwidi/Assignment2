class EBook:
    def __init__(self, title, author, publication_date, genre, price, language, pages):
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price
        self._language = language
        self._pages = pages

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def __str__(self):
        return f"EBook(title={self._title}, author={self._author}, price={self._price})"


class DigitalEBook(EBook):
    def __init__(self, title, author, publication_date, genre, price, language, pages, file_size, format_type):
        super().__init__(title, author, publication_date, genre, price, language, pages)
        self._file_size = file_size
        self._format_type = format_type

    def get_file_size(self):
        return self._file_size

    def set_file_size(self, file_size):
        self._file_size = file_size

    def get_format_type(self):
        return self._format_type

    def set_format_type(self, format_type):
        self._format_type = format_type

    def __str__(self):
        return f"DigitalEBook(title={self._title}, author={self._author}, file_size={self._file_size}MB)"


class Customer:
    def __init__(self, name, contact_info, address, is_loyalty_member=False, referrer=None):
        self._name = name
        self._contact_info = contact_info
        self._address = address
        self._is_loyalty_member = is_loyalty_member
        self._referrer = referrer  # unary relationship for referral

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    def get_is_loyalty_member(self):
        return self._is_loyalty_member

    def set_is_loyalty_member(self, status):
        self._is_loyalty_member = status

    def __str__(self):
        return f"Customer(name={self._name}, contact_info={self._contact_info})"


class ShoppingCart:
    def __init__(self, customer):
        self._customer = customer  # binary association with Customer
        self._items = []
        self._cart_id = f"CART-{customer.get_name()}"

    def add_item(self, ebook):
        self._items.append(ebook)

    def remove_item(self, ebook):
        self._items.remove(ebook)

    def get_items(self):
        return self._items

    def calculate_total(self):
        return sum(item.get_price() for item in self._items)

    def __str__(self):
        items_str = ', '.join(str(item) for item in self._items)
        return f"ShoppingCart(customer={self._customer}, items=[{items_str}])"


class Order:
    def __init__(self, customer, shopping_cart, order_date, status):
        self._customer = customer
        self._shopping_cart = shopping_cart  # aggregation relationship
        self._order_date = order_date
        self._status = status
        self._invoice = None  # composition with Invoice

    def generate_invoice(self):
        self._invoice = Invoice(self)
        return self._invoice

    def get_customer(self):
        return self._customer

    def get_shopping_cart(self):
        return self._shopping_cart

    def __str__(self):
        return f"Order(customer={self._customer}, order_date={self._order_date}, status={self._status})"


class Invoice:
    def __init__(self, order):
        self._order = order
        self._vat_rate = 0.08
        self._discount = 0.0
        self._total_amount = self.calculate_total()

    def calculate_total(self):
        total = self._order.get_shopping_cart().calculate_total()
        self._discount = self.calculate_discount(total)
        total_after_discount = total - self._discount
        vat = total_after_discount * self._vat_rate
        return total_after_discount + vat

    def calculate_discount(self, total):
        if self._order.get_customer().get_is_loyalty_member():
            return total * 0.10
        return 0.0

    def __str__(self):
        return f"Invoice(total_amount={self._total_amount}, discount={self._discount})"


class Discount:
    def __init__(self, loyalty_discount=0.1, bulk_discount=0.2):
        self._loyalty_discount = loyalty_discount
        self._bulk_discount = bulk_discount

    def apply_loyalty_discount(self, total):
        return total * (1 - self._loyalty_discount)

    def apply_bulk_discount(self, total, item_count):
        if item_count >= 5:
            return total * (1 - self._bulk_discount)
        return total

    def __str__(self):
        return f"Discount(loyalty_discount={self._loyalty_discount}, bulk_discount={self._bulk_discount})"

