import products
import store


def make_order():
    """
    Asks the user to place an order and returns the total price.
    """
    order_list = []
    total_price = 0
    print("----------\nWhen you want to finish the order, enter an empty text.")
    while True:
        product_num = input("Which product # do you want? (Enter to finish)")
        if not product_num:
            break
        try:
            product_index = int(product_num) - 1
            selected_product = best_buy.products[product_index]

            quantity = input("What amount do you want?")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Invalid quantity. Please enter a positive integer.")
                if quantity > selected_product.quantity:
                    raise ValueError("Insufficient quantity in stock.")
            except ValueError as e:
                print(e)
                continue

            if quantity > selected_product.quantity:
                print("Insufficient quantity in stock.")
                continue

            selected_product.quantity -= quantity
            total_price += selected_product.price * quantity

            if selected_product.quantity == 0:
                best_buy.remove_product(selected_product)

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
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start()
