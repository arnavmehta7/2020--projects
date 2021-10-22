from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path=r"E:\Whatsapp Automation\All Codes\geckodriver.exe")
driver.get(r"E:\Whatsapp Automation\All Codes\test") ## file:/// as it is our file

# find elements by ID
# form = driver.find_element_by_id(r"form1")

# find with names
# ename = driver.find_element_by_name(r"name")
# ename.send_keys("asas")

# find with link_text
# e2 = driver.find_elements_by_link_text("View help")
# e2.click()