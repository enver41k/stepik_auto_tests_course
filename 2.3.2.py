from selenium.webdriver.common.by import By
from config import browser
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
link2 = "http://suninjuly.github.io/redirect_page.html?"
journey_button_xpath = (By.XPATH, "/html/body/form/div/div/button")


def calc(x):
    return math.log(abs(12 * math.sin(x)))


browser.get(link)

prase = (By.XPATH, "//*[@id='price']")
wait = WebDriverWait(browser, 20)
wait.until(EC.text_to_be_present_in_element(prase, "100"))
browser.find_element(By.XPATH, "//*[@id='book']").click()
x_element = browser.find_element(By.XPATH,'//*[@id="input_value"]')
x = calc(int(x_element.text))
browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(x)
browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
print(browser.switch_to.alert.text)


def main():
    browser.quit()
#
#
if __name__ == "__main__":
    main()
