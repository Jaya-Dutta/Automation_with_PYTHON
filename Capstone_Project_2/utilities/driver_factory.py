from configparser import ConfigParser
from pathlib import Path

from selenium import webdriver


config_file = Path(__file__).resolve().parent.parent / "config" / "config.ini"


def create_driver():
    config = ConfigParser()
    config.read(config_file)

    browser = config["browser"]["name"]
    headless = config["browser"].getboolean("headless")

    if browser.lower() != "chrome":
        raise ValueError("Only Chrome browser is supported")

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    return driver