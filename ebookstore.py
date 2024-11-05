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
