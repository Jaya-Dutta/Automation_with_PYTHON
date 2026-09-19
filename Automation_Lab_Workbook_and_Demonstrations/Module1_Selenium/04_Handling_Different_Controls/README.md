# 1.4 Handling Different Controls on Web Page

## Objective

Understand XPath and learn how to interact with common web controls such as buttons, input boxes, checkboxes, radio buttons and select boxes.

---

## 1. What is XPath?

XPath (XML Path Language) is a locator technique used to find elements in an HTML/XML document.

It is useful when an element does not have a suitable unique ID, name or CSS selector.

Basic syntax:

```text
//tagname[@attribute='value']
```

Example:

```python
driver.find_element(By.XPATH, "//input[@id='username']")
```

---

## 2. Absolute XPath vs Relative XPath

### Absolute XPath

Starts from the root of the HTML document and follows the complete hierarchy.

Example:

```text
/html/body/div/form/input
```

Problems:

* Very long
* Difficult to maintain
* Breaks easily when page structure changes

### Relative XPath

Starts from anywhere in the document using `//`.

Example:

```text
//input[@id='username']
```

Relative XPath is generally preferred because it is shorter and more maintainable.

---

## 3. XPath Contains

`contains()` is useful when only part of an attribute value is known.

Syntax:

```text
//tagname[contains(@attribute,'value')]
```

Example:

```python
driver.find_element(
    By.XPATH,
    "//input[contains(@id,'user')]"
)
```

This can be useful for dynamic attribute values.

---

## 4. XPath Starts-With

`starts-with()` finds an element whose attribute starts with a specific value.

Syntax:

```text
//tagname[starts-with(@attribute,'value')]
```

Example:

```python
driver.find_element(
    By.XPATH,
    "//input[starts-with(@id,'user')]"
)
```

---

## 5. Parent and Sibling Nodes

XPath can navigate between related elements.

Example HTML:

```html
<div>
    <label>Username</label>
    <input type="text">
</div>
```

Parent:

```text
//input/parent::div
```

Following sibling:

```text
//label/following-sibling::input
```

Parent and sibling relationships are useful when the target element does not have a unique attribute.

---

## 6. Handling an Input Box

An input box is used to enter text.

Example:

```python
username = driver.find_element(By.ID, "username")
username.send_keys("Jaya")
```

To clear existing text:

```python
username.clear()
```

To enter new text:

```python
username.send_keys("New Value")
```

---

## 7. Handling a Button

A button can be clicked using Selenium.

Example:

```python
button = driver.find_element(By.ID, "login")
button.click()
```

Buttons are commonly used for:

* Login
* Submit
* Search
* Save
* Next

---

## 8. Handling a Checkbox

A checkbox allows the user to select or deselect an option.

Example:

```python
checkbox = driver.find_element(By.ID, "terms")
checkbox.click()
```

Before clicking, its current state can be checked:

```python
if not checkbox.is_selected():
    checkbox.click()
```

`is_selected()` returns:

```text
True  → selected
False → not selected
```

---

## 9. Handling a Radio Button

A radio button is normally used when only one option should be selected from a group.

Example:

```python
radio = driver.find_element(By.ID, "male")

if not radio.is_selected():
    radio.click()
```

`is_selected()` checks whether the radio button is currently selected.

---

## 10. Handling a Select Box

A standard HTML `<select>` element can be handled using Selenium's `Select` class.

Import:

```python
from selenium.webdriver.support.ui import Select
```

Example:

```python
dropdown = Select(
    driver.find_element(By.ID, "country")
)
```

Select by visible text:

```python
dropdown.select_by_visible_text("India")
```

Select by value:

```python
dropdown.select_by_value("IN")
```

Select by index:

```python
dropdown.select_by_index(1)
```

---

## 11. Common Select Methods

Some useful methods are:

```text
select_by_visible_text()
select_by_value()
select_by_index()
deselect_by_visible_text()
deselect_all()
```

`deselect_*` methods are mainly useful for multi-select dropdowns.

---

## 12. Checking Element Properties

Selenium provides methods to check the state of an element.

```python
element.is_displayed()
element.is_enabled()
element.is_selected()
```

Meaning:

```text
is_displayed() → element is visible
is_enabled()   → element can be interacted with
is_selected()  → checkbox/radio is selected
```

---

## 13. Example: Login Form

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
)

username.send_keys("Jaya")
password.send_keys("password")
login_button.click()

driver.quit()
```

The general flow is:

```text
Open browser
    ↓
Open web page
    ↓
Locate elements
    ↓
Enter data
    ↓
Click button
    ↓
Verify result
    ↓
Close browser
```

---

## 14. Important XPath Examples

```text
//input[@id='username']

//input[@name='password']

//button[@type='submit']

//button[contains(@class,'login')]

//input[starts-with(@id,'user')]

//label/following-sibling::input
```

---

## Key Takeaways

* XPath is a powerful way to locate web elements.
* Relative XPath is generally preferred over absolute XPath.
* `contains()` helps locate elements using partial attribute values.
* `starts-with()` helps with attributes that begin with a known value.
* XPath can navigate through parent and sibling relationships.
* Input boxes use `send_keys()` and `clear()`.
* Buttons use `click()`.
* `is_selected()` checks checkbox/radio state.
* The `Select` class is used for standard HTML select boxes.
* `is_displayed()`, `is_enabled()` and `is_selected()` help verify element state.
