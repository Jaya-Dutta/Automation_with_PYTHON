from utilities.csv_reader import read_csv
from pages.home_page import HomePage
from pages.login_page import LoginPage


test_data = read_csv("testdata.csv")


def test_valid_login(driver):
    data = test_data[0]

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open("https://automationexercise.com")
    home.go_to_login()

    login.login(data["username"], data["password"])

    assert login.is_logged_in()

    login.logout()