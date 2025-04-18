import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import keyboard

driver = webdriver.Firefox()# .Chrome()
file_path = "C:\\Users\\GAMING PC\\PycharmProjects\\ebay_shop_automations\\oestern_.png"


def manualLogin():
    driver.get("https://signin.ebay.de")
    driver.implicitly_wait(5)  # 5 seconds max timeout for all process
    driver.maximize_window()
    input("Login to your ebay seller page, then press enter")
    #driver.find_element(By.ID, "gh-logo").click()

def toSellerPage():
    driver.find_element(By.CSS_SELECTOR, ".gh-my-ebay__link").click()
    driver.find_element(By.XPATH, "//button[text()='Verkaufen']").click()
    driver.find_element(By.XPATH, "//a[text()='Verkauft']").click()

def chooseTimeRoom():
    print("Time room: to be done")

def getSoldElementsAndSendFile():
    # create list of webelements for sold products
    soldElements = driver.find_elements(By.XPATH, "(//a[text()='Einzelheiten zum Kauf ansehen'])")

    # iterate over the different sells
    for soldElement in soldElements:
        # open sell details into new tab and focus on it
        driver.execute_script("arguments[0].scrollIntoView()", soldElement)
        soldElement.send_keys(Keys.CONTROL + Keys.RETURN)
        open_windows = driver.window_handles
        driver._switch_to.window(open_windows[1])

        # click on send message element
        driver.find_element(By.CSS_SELECTOR, ".fake-btn.fake-btn--secondary").click()

        # click on upload image button and select the image you want to upload
        driver.find_element(By.CSS_SELECTOR, "#imageupload__plusIcon").click()
        time.sleep(2)
        keyboard.write(file_path)
        keyboard.press_and_release('return')
        time.sleep(5)

        # send the message
        driver.find_element(By.CSS_SELECTOR, "#imageupload__send--button").click()
        time.sleep(5)
        driver.close()

        # come back to original window and the proceed to next sell
        driver._switch_to.window(open_windows[0])


manualLogin()
toSellerPage()
getSoldElementsAndSendFile()

time.sleep(5)
driver.close()

