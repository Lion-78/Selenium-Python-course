from selenium import webdriver
import time
from math import log, sin


def calc(x_):
    return log(abs(12 * sin(x_)))


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # press the button
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # find value "x"
    x_element = browser.find_element_by_css_selector("#input_value")
    x = int(x_element.text)
    y = calc(x)

    # input value "x" in text_input
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    # press the button "Submit"
    button_submit = browser.find_element_by_css_selector("[type=submit]")
    button_submit.click()

    ## switch to window with alert
    #alert = browser.switch_to.alert
    ## get text from alert
    #text_stepik = alert.text
    #alert.accept()


finally:

    time.sleep(10)
    browser.quit()
