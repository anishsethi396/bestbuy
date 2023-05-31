class Product:
    def __init__(self, name: str, price: float, quantity: int):
        assert quantity > 0, f"Quantity {quantity} is not greater than Zero."
        if not name:
            raise ValueError("Name cannot be empty.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Return the quantity variable in float.
        """
        return float(self.quantity)

    def set_quantity(self, quantity):
        """
        Setter function for quantity and also deactivates the product
        if the quantity reaches zero.
        """
        self.quantity = quantity
        if quantity <= 0:
            self.deactivate()

    def is_active(self):
        """
        Return the status of the product whether it is active or not.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Return a string that represents the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        This function decrease the quantity if the user buys them
        and also returns the total price.
        """
        self.quantity -= quantity
        total_price = self.price * quantity
        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()





