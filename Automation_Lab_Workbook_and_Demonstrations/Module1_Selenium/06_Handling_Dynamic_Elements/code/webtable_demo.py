import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# SETUP
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:
    # 1. WORKING WITH WEBTABLE

    print("\n--- 1. Working with WebTable ---")

    driver.get("https://the-internet.herokuapp.com/tables")

    # Locate the first table
    table = wait.until(
        EC.presence_of_element_located(
            (By.ID, "table1")
        )
    )

    print("WebTable found successfully")
    # 2. READ TABLE HEADERS
    print("\n--- 2. Reading Table Headers ---")

    headers = table.find_elements(
        By.TAG_NAME,
        "th"
    )

    header_names = [header.text for header in headers]

    print("Headers:", header_names)

    # Verify headers exist
    assert len(header_names) > 0

    print("Header verification: PASS")

    # 3. FIND ROWS AND COLUMNS DYNAMICALLY
    # ========================================================

    print("\n--- 3. Rows and Columns ---")

    rows = table.find_elements(
        By.CSS_SELECTOR,
        "tbody tr"
    )

    print("Total rows:", len(rows))

    # Read number of columns from first row
    columns = rows[0].find_elements(
        By.TAG_NAME,
        "td"
    )

    print("Columns per row:", len(columns))

    assert len(rows) > 0
    assert len(columns) > 0

    print("Row / Column verification: PASS")


    # ========================================================
    # 4. TRAVERSE COMPLETE WEBTABLE
    # ========================================================

    print("\n--- 4. Traversing Complete WebTable ---")

    for row_number, row in enumerate(rows, start=1):

        cells = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        row_data = [
            cell.text.strip()
            for cell in cells
        ]

        print(f"Row {row_number}:", row_data)

    print("Complete table traversal: PASS")


    # ========================================================
    # 5. FIND SPECIFIC ROW / CELL
    # ========================================================

    print("\n--- 5. Finding Specific Cell ---")

    # Find a cell containing a specific name
    target_cell = table.find_element(
        By.XPATH,
        ".//td[text()='John']"
    )

    print("Found cell:", target_cell.text)

    assert target_cell.text == "John"

    print("Specific cell verification: PASS")


    # ========================================================
    # 6. VALIDATE TABLE DATA
    # ========================================================

    print("\n--- 6. Table Data Validation ---")

    all_table_text = table.text

    # Verify expected data exists in the table
    assert "John" in all_table_text
    assert "Doe" in all_table_text

    print("Expected data found in table")
    print("Table data validation: PASS")


    # ========================================================
    # FINAL RESULT
    # ========================================================

    print("\n========================================")
    print("WEBTABLE DEMO PASSED SUCCESSFULLY")
    print("========================================")


finally:
    time.sleep(5)  # Optional: Pause to view results before closing
    driver.quit()