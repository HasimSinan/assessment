# Coding Challenge: Fake Coin Detection Using Selenium WebDriver
### Overview

This project is designed to solve the coding challenge of identifying a fake coin among a set of coins using Selenium WebDriver for browser automation. The solution simulates the process of weighing coins on a digital scale to determine which one is fake. The code dynamically interacts with a web-based interface to perform multiple weighings and ultimately identify the fake coin.


### Challenge Description

Given nine coins, where one coin is lighter than the others, the task is to determine which coin is the fake one using a scale. The challenge involves automating this process using Selenium WebDriver, a tool that allows for browser-based automation.
Solution

### The solution involves the following steps:

- Setup and Initialization: The Selenium WebDriver is initialized to interact with the challenge's web-based interface.

- Weighing Process: The coins are divided into groups and weighed against each other to determine which group contains the fake coin.

- Identification: Once the group with the fake coin is identified, individual coins within that group are weighed to find the fake one.
Result: The fake coin is identified, and the result is displayed.


### Prerequisites

Before running the solution, ensure you have the following installed:

- Python 3.x
- Selenium (pip install selenium)
- ChromeDriver (managed via webdriver_manager)
- Google Chrome browser


### Setup and Execution

- Clone the Repository: Clone the repository or download the code files from https://github.com/HasimSinan/assessment

- Install Dependencies: Run the following command to install the necessary Python packages: "pip install selenium webdriver_manager"

- Run the Code: Execute the script using Python:"python <script_name>.py". Replace <script_name> with the name of the Python script file


### Code Explanation

Locators: All locators (e.g., element IDs and XPaths) are defined at the top of the script for easy modification.

Main Functionality:

The coins are divided into three groups.
The first weighing compares two of the groups.
Depending on the result, the fake coin is narrowed down to one group.
A second weighing within the identified group determines the fake coin.
Sleep Intervals: sleep commands are used to ensure that the web elements have enough time to load and reflect changes before the script proceeds.

Result: The script identifies the fake coin and displays its number.


### Troubleshooting

If you encounter any issues while running the script:

- WebDriver Errors: Ensure that the correct version of ChromeDriver is installed and compatible with your Chrome browser version.

- Element Not Found: Verify that the locators match the elements on the webpage. If the webpage structure changes, locators may need to be updated.

- Timeouts: Increase the waiting time in WebDriverWait or the sleep commands if the page is loading slowly.


