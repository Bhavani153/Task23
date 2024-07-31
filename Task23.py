import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# import below keys for actionchains concept
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)
driver.switch_to.frame(0) #there is no frame name so we switch to default frame 0
#ID value for draggable element
d1=driver.find_element(By.ID,"draggable")
#ID value for droppable element
d2=driver.find_element(By.ID,"droppable")
time.sleep(2)
actions = ActionChains(driver)
time.sleep(3)
actions. drag_and_drop(d1,d2)
actions. perform()
time. sleep(3)