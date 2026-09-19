# 1.6 Handling Dynamic Elements

## Objective

Understand how to work with dynamic web elements, check their state, read text and attributes, and extract data from HTML tables.


## 1. What are Dynamic Elements?

Dynamic elements are web elements whose properties or content can change while the page is running.

Examples:

* Dynamic IDs
* AJAX-loaded content
* Changing text
* Elements that become enabled later
* Tables whose rows are generated dynamically

Dynamic elements can make automation difficult because the page structure or element state may change during execution.

---

## 2. Checking Element State

Selenium provides methods to check the current state of an element.

```python
element.is_displayed()
element.is_enabled()
element.is_selected()
```

### is_displayed()

Checks whether the element is visible.

```python
if element.is_displayed():
    print("Element is visible")
```

### is_enabled()

Checks whether the element is enabled for interaction.

```python
if element.is_enabled():
    print("Element is enabled")
```

### is_selected()

Checks whether a checkbox or radio button is selected.

```python
if element.is_selected():
    print("Element is selected")
```

---

## 3. Get Text from an Element

The `.text` property returns the visible text of an element.

Example:

```python
element = driver.find_element(By.ID, "message")
print(element.text)
```

If the HTML is:

```html
<p id="message">Login successful</p>
```

The output is:

```text
Login successful
```

---

## 4. Get Attribute Value

`get_attribute()` is used to read an element's attribute value.

Example:

```python
element = driver.find_element(By.ID, "username")

value = element.get_attribute("value")
print(value)
```

Other examples:

```python
element.get_attribute("id")
element.get_attribute("name")
element.get_attribute("class")
element.get_attribute("href")
```

This is useful when the required information is stored in an HTML attribute rather than visible text.

---

## 5. Difference Between Text and Attribute

Consider:

```html
<input id="username" value="Jaya">
```

Visible text:

```python
element.text
```

For an input field, this may return an empty string because the value is stored in the `value` attribute.

To get the entered value:

```python
element.get_attribute("value")
```

Therefore:

```text
.text
    → visible text

.get_attribute()
    → value stored in an HTML attribute
```

---

## 6. What is a WebTable?

A WebTable is a table displayed on a web page using HTML elements such as:

```html
<table>
<tr>
<td>
<th>
```

Typical table structure:

```text
Table
 ├── Header Row
 │    ├── Name
 │    ├── Status
 │    └── Price
 │
 ├── Data Row
 ├── Data Row
 └── Data Row
```

---

## 7. Locating a WebTable

A table can be located using CSS or XPath.

Example:

```python
table = driver.find_element(
    By.ID,
    "userTable"
)
```

Or:

```python
table = driver.find_element(
    By.XPATH,
    "//table[@id='userTable']"
)
```

---

## 8. Finding Table Rows

Rows are represented by `<tr>`.

```python
rows = table.find_elements(By.TAG_NAME, "tr")
```

This returns a list of table rows.

We can iterate through them:

```python
for row in rows:
    print(row.text)
```

---

## 9. Finding Table Columns

Columns or cells are generally represented by `<td>`.

Example:

```python
cells = row.find_elements(By.TAG_NAME, "td")
```

Then:

```python
for cell in cells:
    print(cell.text)
```

This reads the text from each cell.

---

## 10. Traversing a WebTable

A common approach is:

```python
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    for cell in cells:
        print(cell.text)
```

The flow is:

```text
Find table
    ↓
Find rows
    ↓
Find cells in each row
    ↓
Read cell values
```

---

## 11. Finding a Specific Row

Suppose the table contains:

```text
Name        Status
Jaya        Active
Rahul       Inactive
Priya       Active
```

We can search for a particular name.

Example:

```python
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    if "Jaya" in row.text:
        print(row.text)
```

This identifies the row containing `Jaya`.

---

## 12. Retrieving an Adjacent Value

Suppose the table contains:

```text
Name        Status
Jaya        Active
Rahul       Inactive
```

We can inspect the cells in the matching row:

```python
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    if cells and cells[0].text == "Jaya":
        status = cells[1].text
        print(status)
```

Output:

```text
Active
```

This technique can also be used to retrieve:

* Price
* Status
* Email
* Department
* Stock quantity
* Other related values

---

## 13. Handling Tables with Header Rows

Header cells are commonly represented by `<th>`.

Example:

```python
headers = table.find_elements(By.TAG_NAME, "th")

for header in headers:
    print(header.text)
```

Data rows normally use `<td>` cells.

Therefore:

```text
<th> → Header
<td> → Data cell
<tr> → Row
<table> → Complete table
```

---

## 14. Example: Complete Table Extraction

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

table = driver.find_element(By.ID, "userTable")
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    for cell in cells:
        print(cell.text)

driver.quit()
```

The script:

1. Opens the browser.
2. Opens the web page.
3. Finds the table.
4. Finds all rows.
5. Finds cells inside each row.
6. Prints the cell text.
7. Closes the browser.

---

## 15. Common Problems with Dynamic Elements

Dynamic pages may cause problems such as:

* Element not available immediately.
* Element ID changes.
* Element is temporarily disabled.
* Table content loads after page load.
* Number of rows changes.
* Text changes dynamically.

These problems are commonly handled using:

* Stable locators
* Explicit waits
* Element state checks
* Careful table traversal

Synchronization and waits are covered in the next section.

---

## Key Takeaways

* Dynamic elements can change during page execution.
* `is_displayed()` checks visibility.
* `is_enabled()` checks whether an element can be interacted with.
* `is_selected()` checks checkbox/radio selection.
* `.text` reads visible text.
* `get_attribute()` reads HTML attribute values.
* WebTables are commonly handled by finding the table, rows and cells.
* `<table>` represents the table.
* `<tr>` represents a row.
* `<th>` represents a header cell.
* `<td>` represents a data cell.
* Table rows and cells can be traversed using `find_elements()`.
* Dynamic elements are often handled together with proper synchronization.
