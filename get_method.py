import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

button_enter_user = driver.find_element_by_xpath("//*[@class='navbar__auth navbar__auth_login st-link st-link_style_button ember-link ember-view']")
button_enter_user.click()

textarea_username = driver.find_element_by_xpath("//*[@name='login']")
textarea_username.send_keys("a.untilov@gmail.com")
time.sleep(5)

textarea_password = driver.find_element_by_xpath("//*[@name='password']")
textarea_password.send_keys("hGsyTD9Ez$y@Q2Y")
time.sleep(5)

button_enter = driver.find_element_by_xpath("//*[@class='sign-form__btn button_with-loader ']")
button_enter.click()
time.sleep(20)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea_enter_solution = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea_enter_solution.send_keys("get()")
time.sleep(10)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

button_next_step = driver.find_element_by_xpath("//button[@class='lesson__next-btn button has-icon']")
button_next_step.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
