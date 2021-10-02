import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


message = ""


@pytest.fixture(scope="session")
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(message)

links = {"https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1",
             }


@pytest.mark.parametrize("link", links)
class TestStepikPages():

    def test_page(self, browser, link):
        global message
        browser.get(link)
        input_text = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area")))
        answer = str(math.log(int(time.time())))
        input_text.send_keys(answer)
        button_send = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        button_send.click()
        # time.sleep(20)
        text_result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        text_message_for_each_test = text_result.text
        try:
            assert text_message_for_each_test == "Correct!", "Text not equal 'Correct!'"
        except AssertionError:
            message += text_message_for_each_test
            raise
