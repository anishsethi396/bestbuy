import pytest
import products


def test_normal_product():
    """
    Test case to create a normal product.
    """
    assert products.Product("Test1", price=100, quantity=101)


def test_invalid_details():
    """
    Test case for creating a product with invalid details.
    """
    with pytest.raises(ValueError, match="Name cannot be empty"):
        products.Product("", price=100, quantity=101)

    with pytest.raises(AssertionError, match=f"Price is not greater than Zero"):
        products.Product("Test", price=-100, quantity=101)


def test_product_inactive():
    """
    Test case to check if a product is inactive when its quantity
    is set to zero
    """
    test_product = products.Product("Test", 100, 101)
    assert test_product.is_active() is True

    test_product.set_quantity(0)
    assert test_product.is_active() is False


def test_purchase_modify_quantity():
    """
    Test case to check if the quantity of product change when a user buy it.
    """
    test_product = products.Product("Test", 100, 101)
    test_product.buy(10)
    assert test_product.get_quantity() == 91


def test_buy_large_quantity():
    """
    Test case to check if buying a large quantity of a product
    raises an error.
    """
    test_product = products.Product("Test", 100, 101)
    with pytest.raises(ValueError, match="Insufficient quantity in stock"):
        test_product.buy(110)


pytest.main()
