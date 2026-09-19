# 1.2 Selenium WebDriver Introduction and Installation

## Objective

To understand Selenium WebDriver, its architecture, required software, installation process, browser drivers, and cross-browser execution.


## 1. What is Selenium WebDriver?

Selenium WebDriver is the main Selenium component used for automating modern web browsers.

It allows Python programs to control browsers and perform actions on web applications.

Common actions include:

* Open a webpage
* Find web elements
* Enter text
* Click buttons
* Navigate between pages
* Read page information
* Verify test results


## 2. Selenium 4 WebDriver

Selenium 4 provides the modern WebDriver API for browser automation.

In Python, WebDriver can be imported as:

```python
from selenium import webdriver
```

A browser can then be started using:

```python
driver = webdriver.Chrome()
```

Here, `driver` represents the browser controlled by Selenium.

## 3. WebDriver Architecture

The basic communication flow is:

```text
Python Test Script
        ↓
Selenium WebDriver API
        ↓
Browser Driver / Selenium Manager
        ↓
Web Browser
        ↓
Web Application
```

The Python script sends commands through Selenium WebDriver, which communicates with the browser.


## 4. Software Required

For this course, the main requirements are:

* Python 3
* Selenium 4
* Web Browser
* Code editor such as VS Code
* Python virtual environment

In this workbook, Selenium is installed inside a project-specific `.venv`.



## 5. Selenium Installation with Python

Selenium can be installed using pip:

```powershell
pip install selenium
```

Installation can be verified with:

```powershell
pip show selenium
```

Python import can also be tested using:

```powershell
python -c "import selenium; print(selenium.__version__)"
```


## 6. Browser Drivers in Windows

Traditionally, Selenium required separate browser-driver executables.

Examples:

```text
Chrome  → ChromeDriver
Firefox → GeckoDriver
Edge    → EdgeDriver
```

The driver acts as a communication layer between Selenium and the browser.

Older setups often required the driver executable to be downloaded manually and added to the Windows System PATH.


## 7. Selenium Manager

Modern Selenium includes Selenium Manager, which can automatically help manage compatible browser drivers.

Therefore, for many normal Selenium 4 projects, manually downloading and configuring a driver is not required.

However, understanding manual driver configuration is useful for legacy projects and troubleshooting.

## 8. Running Tests in Different Browsers

Selenium WebDriver supports multiple browsers.

### Chrome

```python
from selenium import webdriver

driver = webdriver.Chrome()
```

### Edge

```python
from selenium import webdriver

driver = webdriver.Edge()
```

### Firefox

```python
from selenium import webdriver

driver = webdriver.Firefox()
```

The same automation logic can generally be reused while changing the browser-specific WebDriver.

---

## 9. Basic Browser Lifecycle

A typical Selenium program follows this flow:

```text
Create WebDriver
      ↓
Open URL
      ↓
Perform actions
      ↓
Verify result
      ↓
Close browser
```

Example:

```python
driver = webdriver.Chrome()
driver.get("https://example.com")

print(driver.title)

driver.quit()
```

`driver.quit()` closes the browser session and releases the associated resources.

## 10. Windows PATH

PATH is an environment variable used by Windows to locate executable programs.

In traditional Selenium setup, adding a browser driver directory to PATH allowed Selenium to find the driver without specifying its complete file location.

Modern Selenium Manager reduces the need for this manual configuration.


## 11. Key Takeaways

* WebDriver is the primary API for modern Selenium browser automation.
* Selenium 4 works with Python through the Selenium package.
* WebDriver communicates with browsers through the appropriate driver mechanism.
* Chrome, Edge, and Firefox can be automated using Selenium.
* Selenium Manager can simplify driver management.
* Windows PATH was commonly used for manually installed browser drivers.
* A WebDriver session should be properly closed using `quit()`.
