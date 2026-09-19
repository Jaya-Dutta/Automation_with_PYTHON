# 1.5 Handling Different Controls on Web Page - Advanced

## Objective

Learn how to handle advanced browser controls such as alerts, datepickers, file uploads, multiple windows or tabs, keyboard actions, scrolling, drag and drop, and IFrames.

## 1. Handling Alert Box

An alert is a browser dialog that displays a message and usually requires user interaction.

Selenium handles alerts using:

```python
alert = driver.switch_to.alert
```

Common operations:

```python
alert.accept()
alert.dismiss()
alert.text
```

Meaning:

```text
accept()  → Clicks OK
dismiss() → Clicks Cancel
text      → Reads alert message
```

Example:

```python
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
```

---

## 2. Handling Confirmation Alert

A confirmation dialog usually contains OK and Cancel options.

Accept:

```python
driver.switch_to.alert.accept()
```

Dismiss:

```python
driver.switch_to.alert.dismiss()
```

Use `accept()` when the OK action is required and `dismiss()` when Cancel is required.

---

## 3. Handling Prompt Alert

A prompt alert allows the user to enter text.

Example:

```python
alert = driver.switch_to.alert
alert.send_keys("Jaya")
alert.accept()
```

The usual flow is:

```text
Trigger prompt
    ↓
Switch to alert
    ↓
Enter text
    ↓
Accept or dismiss
```

---

## 4. Handling Datepicker

A datepicker is a calendar control used to select a date.

The implementation depends on the website.

Common approaches include:

1. Locate the date input and enter a value.
2. Click the calendar and select a date.
3. Navigate through month/year controls.
4. Use XPath or CSS to locate the required date.

Example for a simple input:

```python
date_box = driver.find_element(By.ID, "date")
date_box.send_keys("10/10/2026")
```

For a custom calendar, Selenium may need to click the required month, year and date elements individually.

---

## 5. File Upload

For an HTML file input:

```html
<input type="file">
```

Selenium can upload a file using `send_keys()`.

Example:

```python
file_input = driver.find_element(By.ID, "file")
file_input.send_keys(r"C:\Users\mail2\Documents\sample.pdf")
```

Selenium does not normally control the Windows file-picker dialog directly. Instead, it sends the file path to the HTML `<input type="file">`.

---

## 6. Handling Multiple Windows or Tabs

A browser session can contain multiple windows or tabs.

Selenium provides:

```python
driver.window_handles
```

This returns the window or tab handles available in the current session.

Example:

```python
main_window = driver.current_window_handle

for handle in driver.window_handles:
    driver.switch_to.window(handle)
```

To switch to a specific window:

```python
driver.switch_to.window(handle)
```

---

## 7. Current Window Handle

The currently active window can be identified using:

```python
driver.current_window_handle
```

Example:

```python
main_window = driver.current_window_handle
```

After working with another tab, switch back:

```python
driver.switch_to.window(main_window)
```

---

## 8. Keyboard Events

Selenium provides keyboard keys through the `Keys` class.

Import:

```python
from selenium.webdriver.common.keys import Keys
```

Example:

```python
search_box.send_keys("Selenium")
search_box.send_keys(Keys.ENTER)
```

Other commonly used keys:

```text
Keys.ENTER
Keys.TAB
Keys.ESCAPE
Keys.BACKSPACE
Keys.DELETE
Keys.ARROW_UP
Keys.ARROW_DOWN
Keys.CONTROL
Keys.SHIFT
```

---

## 9. Scrolling

JavaScript can be used to scroll a web page.

Scroll down:

```python
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)
```

Scroll to the top:

```python
driver.execute_script(
    "window.scrollTo(0, 0);"
)
```

Scroll to a specific element:

```python
driver.execute_script(
    "arguments[0].scrollIntoView();",
    element
)
```

---

## 10. Drag and Drop

Selenium provides the `ActionChains` class for advanced mouse interactions.

Import:

```python
from selenium.webdriver.common.action_chains import ActionChains
```

Example:

```python
actions = ActionChains(driver)

actions.drag_and_drop(
    source,
    target
).perform()
```

Here:

* `source` → element to drag
* `target` → element where it should be dropped
* `perform()` → executes the action

---

## 11. IFrames

An IFrame is an HTML document embedded inside another HTML document.

Selenium cannot directly interact with elements inside an IFrame until it switches into that frame.

Example:

```python
iframe = driver.find_element(By.ID, "myFrame")
driver.switch_to.frame(iframe)
```

Now Selenium can interact with elements inside the IFrame.

---

## 12. Switching Back from an IFrame

After completing the interaction, switch back to the main document:

```python
driver.switch_to.default_content()
```

This returns Selenium to the main page.

---

## 13. IFrame Handling Flow

```text
Main Page
    ↓
Locate IFrame
    ↓
Switch to IFrame
    ↓
Interact with elements
    ↓
Switch back to main page
```

Example:

```python
iframe = driver.find_element(By.ID, "myFrame")

driver.switch_to.frame(iframe)

button = driver.find_element(By.ID, "submit")
button.click()

driver.switch_to.default_content()
```

---

## 14. Common Advanced Selenium APIs

| Requirement      | Selenium API                   |
| ---------------- | ------------------------------ |
| Alert            | `driver.switch_to.alert`       |
| Accept alert     | `alert.accept()`               |
| Dismiss alert    | `alert.dismiss()`              |
| Alert text       | `alert.text`                   |
| Upload file      | `send_keys(file_path)`         |
| Window handles   | `driver.window_handles`        |
| Current window   | `driver.current_window_handle` |
| Switch window    | `driver.switch_to.window()`    |
| Keyboard actions | `Keys`                         |
| Mouse actions    | `ActionChains`                 |
| Scroll           | `execute_script()`             |
| Switch to IFrame | `switch_to.frame()`            |
| Exit IFrame      | `switch_to.default_content()`  |

---

## Key Takeaways

* Alerts are handled using `driver.switch_to.alert`.
* `accept()` selects OK and `dismiss()` selects Cancel.
* Prompt alerts can receive text using `send_keys()`.
* File uploads can be performed through an HTML file input.
* `window_handles` helps manage multiple tabs or windows.
* `Keys` is used for keyboard actions.
* `ActionChains` is used for advanced mouse interactions.
* JavaScript can be used for scrolling.
* Elements inside an IFrame require switching into the frame first.
* `default_content()` switches back to the main document.
