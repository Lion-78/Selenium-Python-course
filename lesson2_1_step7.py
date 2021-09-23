import math
from selenium import webdriver
import  time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нахождение картинки с кладом
    img_treasure = browser.find_element_by_id("treasure")

    # получение значения х из значения тега valuex
    x = img_treasure.get_attribute("valuex")

    # вычисление значения функции calc от х
    y = calc(x)

    # заполнение полученного значения функции в текстовое поле
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    # нажатие на флажок (чекбокс) "I'am the robot"
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    # выбор переключателя (radiobutton) "Robots rule"
    people_rule = browser.find_element_by_id("robotsRule")
    people_rule.click()

    # нажатие на кнопку "Submit" ("Подтвердить")
    button_submit = browser.find_element_by_css_selector("[type='Submit']")
    button_submit.click()


finally:
    # задержка 10 секунд
    time.sleep(10)
    # закрытие браузера
    browser.quit()
