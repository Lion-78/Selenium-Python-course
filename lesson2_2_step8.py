import time
from selenium import webdriver
import os


try:

    # open the page in Google Chrome
    link =  "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    registration_data = {"first_name": "Oleksandr", "last_name": "Untilov", "email": "a.untilov@gmail.com"}

    # entering data to the registration form
    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys(registration_data["first_name"])

    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys(registration_data["last_name"])

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys(registration_data["email"])

    # create the file test.txt
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")

    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file.send_keys(file_path)

    # enter the button "Submit"
    button_submit = browser.find_element_by_css_selector("[type='submit']")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
