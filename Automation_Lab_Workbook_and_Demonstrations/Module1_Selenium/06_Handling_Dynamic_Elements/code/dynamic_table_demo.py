import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# SETUP
# ============================================================

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    driver.get("https://the-internet.herokuapp.com/tables")

    table = wait.until(
        EC.presence_of_element_located(
            (By.ID, "table1")
        )
    )


    # ========================================================
    # 1. FIND ROW DYNAMICALLY BY CONDITION
    # ========================================================

    print("\n--- 1. Find Row Dynamically ---")

    # Find the complete row where First Name = John
    john_row = table.find_element(
        By.XPATH,
        ".//tbody/tr[td[2]='John']"
    )

    print("John's row:", john_row.text)

    assert "John" in john_row.text

    print("Dynamic row search: PASS")


    # ========================================================
    # 2. READ CELLS FROM THE DYNAMICALLY FOUND ROW
    # ========================================================

    print("\n--- 2. Read Cells from Dynamic Row ---")

    cells = john_row.find_elements(
        By.TAG_NAME,
        "td"
    )

    last_name = cells[0].text
    first_name = cells[1].text
    email = cells[2].text
    due = cells[3].text

    print("Last Name :", last_name)
    print("First Name:", first_name)
    print("Email     :", email)
    print("Due       :", due)

    assert first_name == "John"
    assert last_name == "Smith"

    print("Dynamic cell extraction: PASS")


    # ========================================================
    # 3. FIND ROW BASED ON A DIFFERENT CONDITION
    # ========================================================

    print("\n--- 3. Find Row Using Due Amount ---")

    target_row = table.find_element(
        By.XPATH,
        ".//tbody/tr[td[4]='$100.00']"
    )

    print("Row with $100.00 due:", target_row.text)

    assert "$100.00" in target_row.text

    print("Condition-based row search: PASS")


    # ========================================================
    # 4. FIND COLUMN INDEX DYNAMICALLY
    # ========================================================

    print("\n--- 4. Find Column Index Dynamically ---")

    headers = table.find_elements(
        By.CSS_SELECTOR,
        "thead th"
    )

    header_names = [
        header.text.strip()
        for header in headers
    ]

    email_column_index = header_names.index("Email") + 1

    print("Email column index:", email_column_index)

    assert "Email" in header_names

    print("Dynamic column identification: PASS")


    # ========================================================
    # 5. GET EMAIL USING DYNAMIC ROW + COLUMN
    # ========================================================

    print("\n--- 5. Dynamic Row + Column Lookup ---")

    john_email = table.find_element(
        By.XPATH,
        f".//tbody/tr[td[2]='John']/td[{email_column_index}]"
    )

    print("John's Email:", john_email.text)

    assert john_email.text == "jsmith@gmail.com"

    print("Dynamic row + column lookup: PASS")


    # ========================================================
    # 6. FINAL VALIDATION
    # ========================================================

    print("\n--- 6. Final Table Validation ---")

    assert "John" in table.text
    assert "jsmith@gmail.com" in table.text
    assert "$100.00" in table.text

    print("All expected dynamic data validated")
    print("Final validation: PASS")


    # ========================================================
    # FINAL RESULT
    # ========================================================

    print("\n========================================")
    print("DYNAMIC TABLE DEMO PASSED SUCCESSFULLY")
    print("========================================")


finally:
    time.sleep(5)  # Optional: Pause to view results before closing
    driver.quit()