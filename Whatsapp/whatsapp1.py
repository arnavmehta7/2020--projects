from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
# driverfire = webdriver.Firefox(executable_path=r'E:\Whatsapp Automation\All Codes\geckodriver.exe')
# driverfire.get(r"https://web.whatsapp.com")
# s = driverfire.find_elements_by_class_name(r"_3FRCZ")
# s[0].send_keys("arshi" + Keys.ENTER)

# s[1].send_keys("Hi"+Keys.ENTER)

# drichro = webdriver.Chrome(executable_path=r"E:\Whatsapp Automation\All Codes\chromedriver.exe")



  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome(executable_path=r'E:\Whatsapp Automation\All Codes\chromedriver.exe') 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 1000) 

# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = 'Arshi'
  
# Replace the below string with your own message 
# string = "Message sent using Python!!!"
  
# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
# group_title.click() 
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
# for i in range(100): 
#     input_box.send_keys(string + Keys.ENTER) 
#     time.sleep(1) 

search = driver.find_element_by_class_name(r"_3FRCZ ")
search.send_keys("arshi"+ Keys.ENTER)