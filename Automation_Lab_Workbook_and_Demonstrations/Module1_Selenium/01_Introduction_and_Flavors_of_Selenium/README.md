# 1.1 Introduction and Different Flavors of Selenium

## Objective --
To understand Selenium, its purpose, major components, browser drivers, and how Selenium is used for web automation.

## 1. What is Selenium?

Selenium is an open-source framework used to automate web browsers.

It allows a program to perform actions such as:

* Opening a website
* Finding web elements
* Entering data
* Clicking buttons
* Navigating between pages
* Verifying results

In this course, Selenium will be used with **Python**.

## 2. Why Selenium?

Manual testing becomes repetitive when the same browser actions have to be performed many times.

Selenium helps automate these tasks, making testing:

* Faster
* Repeatable
* Less dependent on manual effort
* Suitable for regression testing
* Useful for cross-browser testing

## 3. Different Flavors of Selenium

### Selenium IDE

Selenium IDE is a browser-based tool that can record and replay user actions.

It is useful for learning and creating simple automation tests without writing much code.

### Selenium RC

Selenium RC (Remote Control) was an older Selenium technology that used a Selenium Server to execute browser commands.

It has been replaced by Selenium WebDriver in modern Selenium automation.

### Selenium WebDriver

WebDriver is the main Selenium component used for modern browser automation.

It allows programming languages such as Python to communicate with browsers and perform actions on web pages.

### Selenium Grid

Selenium Grid is used to run tests across different browsers, operating systems, or machines.

It is especially useful when tests need to run in parallel.

## 4. Basic Browser Drivers

A browser needs a mechanism through which Selenium can communicate with it.

Common browser-driver relationships are:

* Chrome → ChromeDriver
* Firefox → GeckoDriver
* Edge → EdgeDriver

Modern Selenium can often manage the required driver automatically using **Selenium Manager**.

Manual driver configuration is still useful to understand because it is part of traditional Selenium setup.


## 5. Basic Selenium Architecture

A simple Selenium workflow is:

**Python Test → Selenium WebDriver → Browser → Web Application**

The Python program sends commands through Selenium WebDriver, which communicates with the selected browser.

Example actions:

Open Browser
     ↓
Open Website
     ↓
Find Element
     ↓
Perform Action
     ↓
Verify Result
     ↓
Close Browser

## 6. Selenium in This Course

The main technology used in this workbook is:

* Python 3
* Selenium 4
* Selenium WebDriver
* Chrome / Edge / Firefox

The practical work will gradually cover browser control, locators, web controls, waits, dynamic elements, screenshots, exception handling, and advanced interactions.

## 7. Key Takeaways

* Selenium is used for web browser automation.
* WebDriver is the primary Selenium component for modern automation.
* Selenium IDE supports record-and-replay automation.
* Selenium RC is an older Selenium technology.
* Selenium Grid supports distributed and parallel test execution.
* Browser drivers enable browser communication.
* Selenium Manager can automatically manage drivers in modern Selenium.
* Python will be used to create the automation scripts in this workbook.
