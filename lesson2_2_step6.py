import math
from selenium import webdriver
import time


def calc(x_):
    return math.log(abs(12 * math.sin(x_)))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # finding the value of x
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)  # type of "y" integer

    # find the text input field
    text_input = browser.find_element_by_id("answer")

    # scroll the page down
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_input)
    # enter the value of function calc(x) into text input
    text_input.send_keys(str(y))

    # mark the checkbox "I'm the robot"
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    # selection radiobutton "Robots rule"
    robot_radiobutton = browser.find_element_by_id("robotsRule")
    robot_radiobutton.click()

    # press the button "Submit"
    button_submit = browser.find_element_by_xpath("//*[text()='Submit']")
    button_submit.click()


finally:
    time.sleep(10)
    browser.quit()
