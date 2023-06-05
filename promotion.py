from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    A method imposed in all the child class.
    """
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    """
    A promotion that applies a percentage discount to the total
    price of a product.
    """
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = self.percent / 100
        discounted_price = product.price * quantity * (1 - discount)
        return discounted_price


class SecondHalfPrice(Promotion):
    """
    A promotion that applies a discount to the total price of a product,
    where the second half of the quantity is half price.
    """
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity // 2
        half_price_quantity = quantity - full_price_quantity
        discounted_price = (full_price_quantity * product.price) + (half_price_quantity * product.price / 2)

        return discounted_price


class ThirdOneFree(Promotion):
    """
    A promotion that applies a discount to the total price of a product,
    where every third item is free.
    """
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        free_products = quantity // 3
        products_to_pay = quantity - free_products
        total_price = products_to_pay * product.price
        return total_price
