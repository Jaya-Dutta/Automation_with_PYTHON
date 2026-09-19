# 1.7 Synchronization and Wait Types

## Objective

Understand why synchronization is required in Selenium and learn how to use implicit and explicit waits.

## 1. What is Synchronization?

Synchronization means making Selenium wait for the web page or element to reach the required state before performing an action.

Modern web pages often load elements dynamically.

For example:

```text id="3rv8ah"
Open Page
    ↓
Page starts loading
    ↓
API/AJAX request
    ↓
Element appears
    ↓
Selenium interacts with element
```

If Selenium tries to interact before the element is ready, the test may fail.

---

## 2. Why is Synchronization Required?

Without proper synchronization, Selenium may try to:

* Click an element before it appears.
* Enter text before an input is ready.
* Read data before it is loaded.
* Interact with an element that is temporarily unavailable.

This can result in errors such as:

```text id="4s9s48"
NoSuchElementException
ElementNotInteractableException
TimeoutException
```

Therefore, waits make automation more reliable.

---

## 3. Types of Waits

The two important waits covered here are:

```text id="g2j5m9"
Implicit Wait
Explicit Wait
```

---

## 4. Implicit Wait

An implicit wait tells Selenium to wait for a certain amount of time when searching for elements.

Example:

```python id="5xqzj4"
driver.implicitly_wait(10)
```

This tells Selenium to wait up to 10 seconds while trying to find an element.

Example:

```python id="w6ek0n"
driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://example.com")

element = driver.find_element(By.ID, "username")
```

---

## 5. How Implicit Wait Works

Suppose Selenium searches for an element that is not immediately available.

With:

```python id="y4jq2v"
driver.implicitly_wait(10)
```

Selenium can keep searching for the element for up to 10 seconds before failing.

It does not mean Selenium always pauses for 10 seconds.

If the element appears earlier, Selenium can continue immediately.

---

## 6. Explicit Wait

An explicit wait waits for a **specific condition** to become true.

It is more targeted than an implicit wait.

Basic syntax:

```python id="3g3u7q"
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, 10)
```

Then wait for a condition:

```python id="e5q2v7"
element = wait.until(
    expected_condition
)
```

---

## 7. Expected Conditions

Expected conditions are commonly imported from:

```python id="4w9qgd"
from selenium.webdriver.support import expected_conditions as EC
```

Common conditions include:

```text id="h3z4ok"
EC.presence_of_element_located()
EC.visibility_of_element_located()
EC.element_to_be_clickable()
EC.title_contains()
EC.url_contains()
```

---

## 8. Explicit Wait for Element Presence

Example:

```python id="b7e2qk"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.presence_of_element_located(
        (By.ID, "username")
    )
)
```

The wait continues until the element is present in the DOM or the timeout is reached.

---

## 9. Explicit Wait for Visibility

Sometimes an element exists in the DOM but is not visible.

Use:

```python id="n0cv2p"
element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "message")
    )
)
```

This waits until the element is visible.

---

## 10. Explicit Wait for Clickability

To wait until an element can be clicked:

```python id="6hx0u1"
button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)

button.click()
```

This is useful when a button appears but is initially disabled or unavailable for interaction.

---

## 11. Explicit Wait for URL

Selenium can also wait until the URL contains a particular value.

Example:

```python id="xk8r0f"
wait.until(
    EC.url_contains("dashboard")
)
```

This is useful after actions such as login or navigation.

---

## 12. Explicit Wait for Title

Wait until the page title contains specific text:

```python id="m2hx2j"
wait.until(
    EC.title_contains("Dashboard")
)
```

---

## 13. Implicit vs Explicit Wait

| Feature     | Implicit Wait            | Explicit Wait          |
| ----------- | ------------------------ | ---------------------- |
| Scope       | General element searches | Specific condition     |
| Condition   | Element lookup           | User-defined condition |
| Control     | Less precise             | More precise           |
| Typical use | General synchronization  | Dynamic elements       |
| Main API    | `implicitly_wait()`      | `WebDriverWait()`      |

---

## 14. Why Explicit Wait is Often Preferred for Dynamic Elements

Explicit waits allow the test to wait for exactly what is required.

For example:

```python id="0ksm8x"
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "result")
    )
)
```

Instead of blindly waiting for a fixed amount of time, Selenium waits until the required condition is satisfied.

This usually makes tests more efficient and reliable.

---

## 15. Avoid time.sleep()

Example of a fixed delay:

```python id="0z5f7u"
import time

time.sleep(5)
```

This always pauses for 5 seconds, even if the element becomes ready after 1 second.

For Selenium synchronization, prefer:

```python id="p6l0jw"
WebDriverWait(driver, 10).until(...)
```

This waits for the required condition instead of using an unnecessary fixed delay.

---

## 16. Complete Explicit Wait Example

```python id="x3m5j9"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://example.com")

wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "message")
    )
)

print(element.text)

driver.quit()
```

Flow:

```text id="5w9n2r"
Open browser
    ↓
Open page
    ↓
Create explicit wait
    ↓
Wait for required condition
    ↓
Interact with element
    ↓
Verify result
    ↓
Close browser
```

---

## Key Takeaways

* Synchronization prevents Selenium from interacting with elements before they are ready.
* Implicit wait applies generally to element searches.
* Explicit wait is used for a specific condition.
* `WebDriverWait` is used to create an explicit wait.
* `expected_conditions` provides commonly used conditions.
* `visibility_of_element_located()` waits for visibility.
* `element_to_be_clickable()` waits for clickability.
* `url_contains()` and `title_contains()` can synchronize navigation.
* Avoid unnecessary `time.sleep()` for Selenium synchronization.
* Explicit waits are especially useful for dynamic web elements.
