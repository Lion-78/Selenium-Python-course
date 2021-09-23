import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

# считываем значение переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()
    button_submit = browser.find_element_by_css_selector("[type='submit']")
    button_submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
