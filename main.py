import products
import store
import promotion


def make_order():
    """
    Asks the user to place an order and returns the total price.
    """
    order_list = []
    total_price = 0
    limited_product_added = False
    print("----------\nWhen you want to finish the order, enter an empty text.")
    while True:
        product_num = input("Which product # do you want? (Enter to finish)")
        if not product_num:
            break
        try:
            product_index = int(product_num) - 1
            selected_product = best_buy.products[product_index]

            if isinstance(selected_product, products.LimitedProduct):
                if limited_product_added:
                    print("This product cannot be added more than the maximum limit")
                limited_product_added = True

            quantity = input("What amount do you want?")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Invalid quantity. Please enter a positive integer.")

                else:
                    total_price += selected_product.buy(quantity)

            except ValueError as e:
                print(e)
                continue

            order_list.append(selected_product)
            print(f"Added {selected_product.name} to your order.")
        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")

    print(f"\nOrder made! Total payment: ${total_price}")


def start():
    """
   Displays a menu and allow user to input there response.
    """
    menu = ("""
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
    while True:
        print(menu)
        user_input = input("Please choose a number: ")
        if user_input == "1" or user_input == "3":
            all_products = best_buy.get_all_products()
            product_index = 1
            for product in all_products:
                print(f"{product_index}. {product.show()}")
                product_index += 1

        if user_input == "2":
            print(f"\nTotal of {best_buy.get_total_quantity()} items in store")

        if user_input == "3":
            make_order()

        if user_input == "4":
            print("Bye!")
            return False


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotion.SecondHalfPrice("Second Half price!")
    third_one_free = promotion.ThirdOneFree("Third One Free!")
    thirty_percent = promotion.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start()
