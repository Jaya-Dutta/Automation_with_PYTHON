# Module 1.9 – Advanced Interactions

This section covers advanced Selenium interactions and reading and writing test data using common file formats.

## Topics Covered

* Different APIs to read data from Excel and JSON
* Reading data from Properties, CSV, and XML files
* Reading data from Excel and JSON
* Writing data into Excel and JSON
* Mouse Hover Actions
* Executing JavaScript Commands

## 1. Reading Data from Different File Formats

Automation tests may require test data from external files instead of hardcoded values.

Common formats used in automation include:

* Excel
* JSON
* Properties
* CSV
* XML

Python provides different libraries and APIs to work with these file formats.

## 2. Reading Data from Excel

Excel files commonly use the `.xlsx` format.

Python can read Excel data using libraries such as `openpyxl`.

Example:

```python
from openpyxl import load_workbook

workbook = load_workbook("test_data.xlsx")
sheet = workbook["Sheet1"]

value = sheet["A1"].value
print(value)
```

## 3. Reading Data from JSON

JSON is commonly used for storing structured test data and configuration.

Example:

```python
import json

with open("test_data.json", "r") as file:
    data = json.load(file)

print(data["username"])
```

## 4. Reading Properties Files

Properties files can store configuration or test data in key-value format.

Example:

```text
username=Jaya
browser=Chrome
```

Python can read the file as text and process the key-value pairs.

## 5. Reading CSV Files

CSV stands for Comma-Separated Values and is commonly used for tabular test data.

Example:

```python
import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

## 6. Reading XML Files

XML is another structured data format used for storing test data and configuration.

Python provides `xml.etree.ElementTree` for processing XML files.

Example:

```python
import xml.etree.ElementTree as ET

tree = ET.parse("users.xml")
root = tree.getroot()

for element in root:
    print(element.text)
```

## 7. Writing Data into Excel

Data can be written into an Excel sheet using `openpyxl`.

Example:

```python
from openpyxl import load_workbook

workbook = load_workbook("test_data.xlsx")
sheet = workbook["Sheet1"]

sheet["B1"] = "Test Passed"

workbook.save("test_data.xlsx")
```

## 8. Writing Data into JSON

Python can also write structured data into a JSON file.

Example:

```python
import json

data = {
    "status": "Passed",
    "browser": "Chrome"
}

with open("result.json", "w") as file:
    json.dump(data, file, indent=4)
```

## 9. Mouse Hover Actions

Mouse hover means moving the mouse pointer over a web element.

Selenium provides `ActionChains` for performing mouse hover actions.

Example:

```python
from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element(By.ID, "menu")

actions = ActionChains(driver)
actions.move_to_element(menu).perform()
```

Mouse hover can be used for navigation menus, dropdown menus, tooltips, and other hover-based elements.

## 10. Executing JavaScript Commands

Selenium can execute JavaScript commands in the browser using `execute_script()`.

Example:

```python
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)
```

JavaScript execution can be useful for browser interactions such as scrolling or performing specific actions when required.

## File Format and API Summary

| Requirement | Python API / Library    |
| ----------- | ----------------------- |
| Excel       | `openpyxl`              |
| JSON        | `json`                  |
| Properties  | File handling           |
| CSV         | `csv`                   |
| XML         | `xml.etree.ElementTree` |
| Mouse Hover | `ActionChains`          |
| JavaScript  | `execute_script()`      |

## Expected Learning Outcome

After completing this section, the learner should be able to:

* Read test data from Excel and JSON
* Read data from Properties, CSV, and XML files
* Write data into Excel and JSON
* Perform mouse hover actions using Selenium
* Execute JavaScript commands through Selenium

## Result

Advanced Selenium interactions and test-data handling using Excel, JSON, Properties, CSV, XML, mouse hover, and JavaScript commands were studied and demonstrated.
