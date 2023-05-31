import products


class Store:
    """
    This class represents a store which sells products.
    """
    def __init__(self, list_of_products):
        self.products = list_of_products

    def add_product(self, product):
        """
        Add a product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Returns the total quantity of products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return int(total_quantity)

    def get_all_products(self):
        """
        Returns a list of all active products in the store.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list):
        """
        Returns the total_price for the products in the shopping list.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price = product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
