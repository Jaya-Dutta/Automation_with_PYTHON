# 1.8 Taking Screenshots and Exception Handling

## Objective

Learn how to capture screenshots during Selenium execution and handle runtime errors using Python exception handling.


## 1. Taking Screenshots

Screenshots are useful for recording the browser state during test execution.

They help with:

* Debugging failed tests
* Test evidence
* Reporting
* Understanding unexpected page states

Selenium provides:

```python id="5q4x7p"
driver.save_screenshot("screenshot.png")
```

This saves the current browser screen as an image file.



## 2. Taking a Screenshot with a File Path

Example:

```python id="q3x8nd"
driver.save_screenshot(
    "screenshots/home_page.png"
)
```

The screenshot is saved inside the specified folder.

Make sure the folder exists before saving the screenshot.

---

## 3. Screenshot After an Important Action

A screenshot can be taken after actions such as:

```text id="zqj4k1"
Open page
    ↓
Enter data
    ↓
Click button
    ↓
Take screenshot
    ↓
Verify result
```

Example:

```python id="7j6v2h"
driver.get("https://example.com")

driver.save_screenshot(
    "screenshots/page.png"
)
```

---

## 4. Generic Screenshot Method

When a test contains many screenshots, creating a reusable function is better.

Example:

```python id="7w8m3c"
def take_screenshot(driver, filename):
    driver.save_screenshot(
        f"screenshots/{filename}.png"
    )
```

Now it can be reused:

```python id="g4z1ds"
take_screenshot(driver, "login_page")
take_screenshot(driver, "after_login")
```

This avoids repeating the same screenshot code.

---

## 5. What is Exception Handling?

An exception is an error that occurs while a program is running.

Examples:

```text id="4zq8km"
Element not found
Invalid operation
File not found
Timeout
Incorrect input
```

Exception handling allows a program to respond to errors instead of stopping unexpectedly.

---

## 6. try and except

Python uses `try` and `except` for exception handling.

Example:

```python id="x5j2rv"
try:
    element = driver.find_element(
        By.ID,
        "username"
    )
    element.click()

except Exception as e:
    print("Error:", e)
```

The code inside `try` is executed normally.

If an exception occurs, Python executes the `except` block.

---

## 7. finally Block

The `finally` block runs whether an exception occurs or not.

Example:

```python id="m8n6qp"
try:
    print("Test started")

except Exception as e:
    print("Error:", e)

finally:
    print("Test completed")
```

This is useful for cleanup operations.

---

## 8. Selenium Example with try-except-finally

```python id="1b7qxs"
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")

    element = driver.find_element(
        By.ID,
        "username"
    )

    element.send_keys("Jaya")

except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()
```

Here:

* `try` → contains the main test steps.
* `except` → handles an error.
* `finally` → closes the browser.

---

## 9. Handling Specific Exceptions

It is often better to catch a specific exception when the expected error is known.

Example:

```python id="0r3k2v"
from selenium.common.exceptions import NoSuchElementException

try:
    element = driver.find_element(
        By.ID,
        "username"
    )

except NoSuchElementException:
    print("Username element was not found")
```

Some common Selenium exceptions are:

```text id="e5k1p8"
NoSuchElementException
TimeoutException
ElementNotInteractableException
StaleElementReferenceException
```

---

## 10. Screenshot on Test Failure

Screenshots are especially useful when a test fails.

Example:

```python id="n6v2jt"
try:
    driver.get("https://example.com")

    driver.find_element(
        By.ID,
        "wrong_id"
    ).click()

except Exception as e:
    driver.save_screenshot(
        "screenshots/test_failure.png"
    )
    print("Test failed:", e)

finally:
    driver.quit()
```

If an error occurs, the current browser state is captured before the browser is closed.

---

## 11. Why Use finally for driver.quit()?

The browser should be closed even when a test fails.

Without `finally`, an error may occur before `driver.quit()` is reached.

Using:

```python id="x3h7qa"
finally:
    driver.quit()
```

helps ensure that the browser session is cleaned up.

---

## 12. try-except-finally Flow

```text id="w8f2qm"
Start Test
    ↓
try
    ↓
Test Steps
    ↓
Error?
 ┌──Yes──────────────┐
 ↓                   │
except              │
 ↓                   │
Handle Error         │
 └────────┬──────────┘
          ↓
       finally
          ↓
    Cleanup Resources
          ↓
       End Test
```

---

## 13. Screenshot and Exception Handling Together

A practical Selenium test can combine both concepts:

```python id="q9k4tm"
try:
    driver.get("https://example.com")

    element = driver.find_element(
        By.ID,
        "username"
    )

    element.send_keys("Jaya")

except Exception as e:
    driver.save_screenshot(
        "screenshots/error.png"
    )
    print("Error:", e)

finally:
    driver.quit()
```

This provides:

* Error handling
* Failure evidence
* Browser cleanup

---

## Key Takeaways

* Screenshots provide visual evidence of browser execution.
* `save_screenshot()` captures the current browser screen.
* A reusable screenshot function avoids repeated code.
* Exceptions are runtime errors.
* `try` contains the code that may fail.
* `except` handles the exception.
* `finally` runs regardless of success or failure.
* Specific Selenium exceptions can be handled separately.
* Taking a screenshot inside `except` is useful for debugging failed tests.
* `driver.quit()` should be used for proper browser cleanup.
