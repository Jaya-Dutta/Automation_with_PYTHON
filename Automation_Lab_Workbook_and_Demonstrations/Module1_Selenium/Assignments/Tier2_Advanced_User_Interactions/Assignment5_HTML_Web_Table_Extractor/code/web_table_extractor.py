from selenium import webdriver
from selenium.webdriver.common.by import By


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open HTML table practice page
    driver.get("https://the-internet.herokuapp.com/tables")

    # Locate the first web table
    table = driver.find_element(By.ID, "table1")

    # Extract table headers
    headers = [
        header.text
        for header in table.find_elements(By.CSS_SELECTOR, "thead th")
    ]

    # Extract all table rows
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    print("Table Headers:")
    print(headers)

    print("\nTable Data:")

    # Read and print each row
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, "td")
        row_data = [cell.text for cell in cells]
        print(row_data)

    # Basic validation
    assert len(headers) == 6
    assert len(rows) > 0

    print("\nWeb table extracted successfully!")

finally:
    # Close browser
    driver.quit()