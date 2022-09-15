from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path='C:\drivers\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://spot.tecno.com/ng/index.php')

driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div[3]/a[1]').click() #  CLICKS LOGIN
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/div/div[1]/ul/li[1]').click()
# driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/div/div[1]/ul/li[2]').click()


element = driver.find_element_by_name('cc')
dropdown = Select(element)
dropdown.select_by_value('1')
time.sleep(1)
phone = driver.find_element_by_name('account')
phone.send_keys('5018596935')

pswrd = driver.find_element_by_name('pwd')
pswrd.send_keys('Rollings')

driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/div/div[3]/button').click()

time.sleep(1)
foca = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/input')
foca.send_keys('FOCA')
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/i').click()  # CLICKS THE SEARCH
driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td/div/div[2]/ul/li[1]/div[2]/h3/a').click()