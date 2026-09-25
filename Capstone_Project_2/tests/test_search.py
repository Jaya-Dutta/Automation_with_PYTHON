from utilities.csv_reader import read_csv
from pages.home_page import HomePage
from pages.search_page import SearchPage


test_data = read_csv("testdata.csv")


def test_product_search(driver):
    data = test_data[0]

    home = HomePage(driver)
    search = SearchPage(driver)

    home.open("https://automationexercise.com")
    home.go_to_products()

    search.search_product(data["search_product"])

    assert search.is_search_result_visible()

    search.add_product_to_cart(data["expected_product"])