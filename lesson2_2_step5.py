from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # задержка 10 секунд
    time.sleep(10)
    # закрытие браузера
    browser.quit()
