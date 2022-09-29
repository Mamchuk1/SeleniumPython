from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# initialization
driver = webdriver.Chrome('/home/cryptonuser111/Code/PythonSelenium/chromedriver')
driver.maximize_window()

# login
driver.implicitly_wait(10)
driver.get("https://testnet.console.decimalchain.com/")
loginField = driver.find_element(By.TAG_NAME, "textarea")
loginField.send_keys("twenty umbrella bless honey garden sunny vote cream another bacon youth twenty document shoe risk library van slight radar banana argue venture father master")
loginBtn = driver.find_element(By.CLASS_NAME, "box__sign-in-btn" )
loginBtn.click()
#wait var
wait = WebDriverWait(driver, 10)
#to crosschain
crosschain = driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/nav/div/div[1]/div/a[3]")
crosschain.click()
# loop crosschain finding button
for i in range(28):
    try:
        baton = driver.find_element(By.CLASS_NAME, "txs__btn")
        nextPage = driver.find_element(By.XPATH,"//*[@id='__layout']/div/div[1]/div/main/div/div[4]/div/div[2]/div[12]/ul/li[8]")
        if baton.is_displayed():
            baton.click()
            print("wp")
            break
    except NoSuchElementException:
        print("you suck")
        nextPage = driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/main/div/div[4]/div/div[2]/div[12]/ul/li[8]")
        nextPage.click()
