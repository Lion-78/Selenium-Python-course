from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name, last_name, email = 'Alexandr', 'Untilov', 'a.untilov@gmail.com'
    input_1 = browser.find_element_by_xpath("//*[text()='First name*']/following-sibling::input")
    input_1.send_keys(first_name)
    input_2 = browser.find_element_by_xpath("//*[text()='Last name*']/following-sibling::input")
    input_2.send_keys(last_name)
    input_3 = browser.find_element_by_xpath("//*[text()='Email*']/following-sibling::input")
    input_3.send_keys(email)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
