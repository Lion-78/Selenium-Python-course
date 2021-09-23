import time
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
#
#
#    num1_element = browser.find_element_by_id("num1")
#    num2_element = browser.find_element_by_id("num2")
#    str_num1 = num1_element.text
#    str_num2 = num2_element.text
#    summa = int(str_num1) + int(str_num2)
#
#    select_sum = Select(browser.find_element_by_tag_name("select"))
#    select_sum.select_by_value(str(summa))
#    button_submit.click()
#
#
#    button_submit = browser.find_element_by_xpath("//*[text()='Submit']")

    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # задержка 10 секунд
    time.sleep(10)
    # закрытие браузера
    browser.quit()


