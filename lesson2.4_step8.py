from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
btn = browser.find_element(By.ID, "book").click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
y = calc(x)
input1.send_keys(y)

button1 = browser.find_element(By.CSS_SELECTOR, "#solve")
button1.click()
# напечатать код для копирования который выводится после успешного прохождения теста
print(browser.switch_to.alert.text.split()[-1])

time.sleep(10)
browser.quit()

