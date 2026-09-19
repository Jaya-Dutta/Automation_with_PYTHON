# 1.3 Locators and Object Identification

## Objective

Understand web elements and different Selenium locators used to identify elements on a web page.

---

## 1. What is a Web Element?

A web element is any HTML object on a web page that Selenium can interact with.

Examples:

* Input box
* Button
* Checkbox
* Radio button
* Link
* Dropdown
* Text

Example HTML:

```html
<input id="username" name="user" type="text">
```

Here:

* `input` → Tag name
* `id="username"` → ID attribute
* `name="user"` → Name attribute
* `type="text"` → Type attribute

---

## 2. What is a Locator?

A locator tells Selenium **which web element to find** on a page.

Common Selenium locators:

* ID
* Name
* Tag Name
* Link Text
* Partial Link Text
* Class Name
* CSS Selector
* XPath

Basic syntax:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "username")
```

---

## 3. Challenges in Element Identification

Finding elements can be difficult when:

* Multiple elements have similar attributes.
* Elements have dynamic IDs.
* Classes are reused.
* Elements are deeply nested.
* The page contains dynamic content.
* The HTML structure changes.

A good locator should be:

* Unique
* Stable
* Simple
* Easy to maintain

---

## 4. Find Element by ID

ID is usually one of the simplest and preferred locators when the ID is unique and stable.

```python
driver.find_element(By.ID, "username")
```

Example:

```html
<input id="username">
```

---

## 5. Find Element by Name

The `name` attribute can be used to locate an element.

```python
driver.find_element(By.NAME, "password")
```

Example:

```html
<input name="password">
```

---

## 6. Find Element by Tag Name

Tag Name identifies an element using its HTML tag.

```python
driver.find_element(By.TAG_NAME, "input")
```

Example tags:

```text
input
button
a
div
p
```

Tag Name may return an element that is not unique, so it is often combined with other techniques.

---

## 7. Find Element by Link Text

Used to locate a link using its complete visible text.

```python
driver.find_element(By.LINK_TEXT, "Login")
```

Example:

```html
<a href="/login">Login</a>
```

---

## 8. Find Element by Partial Link Text

Used when only part of the link text is known.

```python
driver.find_element(By.PARTIAL_LINK_TEXT, "Log")
```

For example, this can match:

```text
Login
Logout
Login Here
```

Use it carefully when multiple links may match.

---

## 9. Find Element by Class Name

Uses the HTML `class` attribute.

```python
driver.find_element(By.CLASS_NAME, "login-button")
```

Example:

```html
<button class="login-button">Login</button>
```

If an element has multiple classes, using the complete space-separated class string with `CLASS_NAME` is not valid. CSS selectors are better for multiple classes.

---

## 10. Find List of Elements

`find_elements()` returns multiple matching elements as a list.

```python
elements = driver.find_elements(By.TAG_NAME, "input")
```

Example:

```python
for element in elements:
    print(element.get_attribute("type"))
```

Difference:

```text
find_element()  → returns one matching element
find_elements() → returns a list of matching elements
```

If `find_elements()` finds nothing, it returns an empty list.

---

## 11. CSS Selector

CSS selectors provide a powerful way to identify elements.

By ID:

```python
driver.find_element(By.CSS_SELECTOR, "#username")
```

By class:

```python
driver.find_element(By.CSS_SELECTOR, ".login-button")
```

By attribute:

```python
driver.find_element(By.CSS_SELECTOR, "input[name='username']")
```

---

## 12. Wildcards with CSS Selectors

CSS wildcard selectors can be useful when only part of an attribute value is known.

Starts with:

```css
input[id^='user']
```

Contains:

```css
input[id*='user']
```

Ends with:

```css
input[id$='name']
```

Example:

```python
driver.find_element(
    By.CSS_SELECTOR,
    "input[id^='user']"
)
```

---

## 13. Child Nodes Using CSS Selectors

CSS selectors can identify child elements.

Direct child:

```css
div > input
```

This means:

```text
input is a direct child of div
```

Descendant:

```css
div input
```

This means:

```text
input exists somewhere inside div
```

Example:

```python
driver.find_element(
    By.CSS_SELECTOR,
    "form > input"
)
```

---

## 14. Basic Locator Priority

A practical preference is:

```text
Unique ID
   ↓
Name
   ↓
Stable CSS Selector
   ↓
Link Text
   ↓
XPath
   ↓
Other approaches
```

The best locator is not always the shortest one. It should be **unique, stable, readable, and maintainable**.

---

## 15. Important Selenium Syntax

```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "username")
element.send_keys("Jaya")
```

Here:

* `By.ID` → tells Selenium which locator strategy to use.
* `"username"` → value of the locator.
* `find_element()` → searches for the element.
* `send_keys()` → enters text into the element.


## Key Takeaways

* Locators help Selenium identify web elements.
* ID is usually preferred when it is unique and stable.
* Name, Tag Name, Link Text, Partial Link Text and Class Name are other basic locators.
* `find_element()` finds one element.
* `find_elements()` returns multiple elements as a list.
* CSS selectors are powerful and readable.
* CSS supports attribute matching and child selection.
* Good locators should be unique, stable and maintainable.
* XPath will be covered in the next section.
