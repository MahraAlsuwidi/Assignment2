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
