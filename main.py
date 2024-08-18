from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Locators and coin groups
left_square_1 = "left_0"
left_square_2 = "left_1"
left_square_3 = "left_2"
right_square_1 = "right_0"
right_square_2 = "right_1"
right_square_3 = "right_2"
weigh_button = "weigh"
reset_button = "//*[text()='Reset']"

# Divided coins into 3 groups to be able to weigh in minimum repetition
coin_groups = {
    "group_1": [0, 1, 2],
    "group_2": [3, 4, 5],
    "group_3": [6, 7, 8]
}


def initialize_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://sdetchallenge.fetch.com/")
    return driver


def perform_weighing(driver, left_group, right_group):
    # Clear previous inputs
    clear_scales(driver)

    # Fill the left and right scales with the respective groups
    for i, coin in enumerate(left_group):
        driver.find_element(By.ID, f'left_{i}').send_keys(str(coin))
    for i, coin in enumerate(right_group):
        driver.find_element(By.ID, f'right_{i}').send_keys(str(coin))

    # Click the "Weigh" button and get the result
    driver.wait.until(EC.element_to_be_clickable((By.ID, weigh_button))).click()
    sleep(2)  # Used sleep method to ensure result is loaded. I tried various wait methods, but without success.
    result = driver.find_element(By.XPATH, "//div[@class='result']//button[@id='reset']").text
    reset_scales(driver)
    return result


def clear_scales(driver):
    # Clear the scales before placing new coins
    for i in range(3):
        driver.find_element(By.ID, f'left_{i}').clear()
        driver.find_element(By.ID, f'right_{i}').clear()


def reset_scales(driver):
    # Reset the scales for the next weighing
    driver.find_element(By.XPATH, reset_button).click()


def determine_fake_coin(driver, group, weigh_results):
    # Weigh the first two coins in the group
    result = perform_weighing(driver, [group[0]], [group[1]])
    weigh_results.append(result)  # Capture the result of this weighing

    if result == '<':
        return group[0]
    elif result == '>':
        return group[1]
    else:
        return group[2]


def main():
    driver = initialize_driver()

    weigh_results = []

    try:
        # First weighing between group_1 and group_2
        result = perform_weighing(driver, coin_groups["group_1"], coin_groups["group_2"])
        weigh_results.append(result)  # Capture the result of the first weighing

        # Determine which group contains the fake coin and weigh within that group
        if result == '<':
            fake_coin = determine_fake_coin(driver, coin_groups["group_1"], weigh_results)
        elif result == '>':
            fake_coin = determine_fake_coin(driver, coin_groups["group_2"], weigh_results)
        else:
            fake_coin = determine_fake_coin(driver, coin_groups["group_3"], weigh_results)

        # Click the fake coin and handle the alert
        driver.wait.until(EC.element_to_be_clickable((By.ID, f'coin_{fake_coin}'))).click()
        alert_text = Alert(driver).text
        print(f'Alert message is "{alert_text}"')

    finally:
        driver.quit()

    # Print the number of weighings and their results
    print(f"Total number of weighings: {len(weigh_results)}")
    print("Weighing results:")
    for i, result in enumerate(weigh_results, 1):
        print(f"Weighing {i}: {result}")

    # Print the fake coin number
    print(f"Fake coin: {fake_coin}")


main()
