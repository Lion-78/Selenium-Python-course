from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
from time import sleep

def calc(x):
    return log(abs(12 * sin(x)))

def function_math():

    # find value "x"
    x_element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input_value")))
    x = int(x_element.text)
    y = calc(x)

    # input value "x" in text_input
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    # press the button "Submit"
    button_submit = browser.find_element_by_css_selector("[type=submit]")
    button_submit.click()


try:

    # open the page
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # wait until button is clickable
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID,"book")))
    price_element = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button.click()

    function_math()



finally:
    sleep(5)
    browser.quit()
