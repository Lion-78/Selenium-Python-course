"""
Вариант немного усложненный по сравнению с заданием в шаге 4.
Добавлена авторизация в Степике и потом ввод числа, полученного в задании, в поле ввода ответа в шаге (задании).
"""
from math import log, sin
from selenium import webdriver
import time

def calc(x_):
    return log(abs(12 * sin(x_)))


try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # press the button
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # switch to window with alert
    alert1 = browser.switch_to.alert
    # accept alert
    alert1.accept()

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

    # switch to window with alert
    alert2 = browser.switch_to.alert
    # get text from alert
    text_stepik = alert2.text
    alert2.accept()

    # put answer from string alert text
    answer_stepik = text_stepik.split(": ")[-1]

#    time.sleep(10)
#    browser.close()

    # Authorisation in Stepik

    link_autorisation_stepik = "https://stepik.org/course/575/promo"
    browser.get(link_autorisation_stepik)
    time.sleep(10)

    button_enter_user = browser.find_element_by_xpath(
        "//*[@class='navbar__auth navbar__auth_login st-link st-link_style_button ember-link ember-view']")
    button_enter_user.click()
    time.sleep(5)

    textarea_username = browser.find_element_by_xpath("//*[@name='login']")
    textarea_username.send_keys("a.untilov@gmail.com")
    time.sleep(5)

    textarea_password = browser.find_element_by_xpath("//*[@name='password']")
    textarea_password.send_keys("hGsyTD9Ez$y@Q2Y")
    time.sleep(5)

    button_enter = browser.find_element_by_xpath("//*[@class='sign-form__btn button_with-loader ']")
    button_enter.click()
    time.sleep(20)

    link_stepik = "https://stepik.org/lesson/184253/step/4?unit=158843"
    browser.get(link_stepik)
    time.sleep(5)

    # text input on stepik
    text_input_stepik = browser.find_element_by_css_selector(".textarea")
    text_input_stepik.send_keys(answer_stepik)

    submit_button = browser.find_element_by_css_selector(".submit-submission")

    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()
    time.sleep(5)

    # press the button "Next step"
    button_next_step = browser.find_element_by_xpath("//a[@href='/lesson/184253/step/5?unit=158843']")
    button_next_step.click()



finally:

    time.sleep(10)
    browser.quit()
