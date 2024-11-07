from ebookstore import EBook, Customer, ShoppingCart, Order,DigitalEBook
def test_ebookstore():
    ebook1 = DigitalEBook("Python Programming", "John Doe", "2023-01-01", "Programming", 29.99, "English", 500, 5, "PDF")
    ebook2 = DigitalEBook("Learning AI", "Jane Smith", "2023-02-15", "AI", 39.99, "English", 300, 8, "ePub")

    customer = Customer("Ahmad", "ahmad@gmail.com", "123 Main St", is_loyalty_member=True)

    cart = ShoppingCart(customer)
    cart.add_item(ebook1)
    cart.add_item(ebook2)

    order = Order(customer, cart, "2023-10-01", "Confirmed")
    invoice = order.generate_invoice()

    print(cart)
    print(order)
    print(invoice)


test_ebookstore()
