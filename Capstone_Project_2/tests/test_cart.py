from utilities.csv_reader import read_csv
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.cart_page import CartPage


test_data = read_csv("testdata.csv")


def test_product_in_cart(driver):
    data = test_data[0]

    home = HomePage(driver)
    search = SearchPage(driver)
    cart = CartPage(driver)

    home.open("https://automationexercise.com")
    home.go_to_products()

    search.search_product(data["search_product"])

    assert search.is_search_result_visible()

    search.add_product_to_cart(data["expected_product"])
    search.open_cart_from_modal()

    assert cart.is_cart_visible()
    assert cart.is_product_visible(data["expected_product"])