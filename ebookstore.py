class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

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

class Customer:
    def __init__(self, name, contact_info, is_loyalty_member=False):
        self._name = name
        self._contact_info = contact_info
        self._is_loyalty_member = is_loyalty_member

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
        self._customer = customer
        self._items = []

    def add_item(self, ebook):
        self._items.append(ebook)

    def remove_item(self, ebook):
        self._items.remove(ebook)

    def update_item_quantity(self, ebook, quantity):
        if ebook in self._items:
            self.remove_item(ebook)
            self.add_item(ebook)

    def get_items(self):
        return self._items
    def calculate_total(self):
        total = 0
        for ebook in self._items:
            total += ebook.get_price()
        return total

    def __str__(self):
        items_str = ''
        for item in self._items:
            items_str += str(item) + ', '
        items_str = items_str[:-2]
        return f"ShoppingCart(customer={self._customer}, items=[{items_str}])"

class Order:
    def __init__(self, customer, shopping_cart, order_date):
        self._customer = customer
        self._shopping_cart = shopping_cart
        self._order_date = order_date
        self._invoice = None

    def generate_invoice(self):
        self._invoice = Invoice(self)
        return self._invoice

    def get_customer(self):
        return self._customer

    def get_shopping_cart(self):
        return self._shopping_cart

    def __str__(self):
        return f"Order(customer={self._customer}, order_date={self._order_date})"

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
