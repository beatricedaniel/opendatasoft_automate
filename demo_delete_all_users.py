# modules pour interagir avec le navigateur
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# modules pour ralentir les requêtes
from random import randint 
from time import sleep  
# module pour la navigation headless
from selenium.webdriver.chrome.options import Options
# # rotation de proxys
# from fake_useragent import UserAgent

# # Initialisation du faux user-agent
# ua = UserAgent()
# user_agent =ua.random

# Rendre le navigateur headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
# # Rendre le user-agent aléatoire
# chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('C:/Users/beatrice.daniel/Downloads/chromedriver_win32/chromedriver.exe', options=chrome_options)

driver.get("https://***.opendatasoft.com/backoffice/security/users/")
sleep(randint(2,5))
enter_username = driver.find_element_by_id('username')
enter_username.send_keys('***')
sleep(randint(2,5))
enter_password = driver.find_element_by_id('password')
enter_password.send_keys('***')
sleep(randint(2,5))
sign_in = driver.find_element_by_class_name('ods-button')
sign_in.click()
sleep(randint(2,5))

def delete_loop():
    users = driver.find_elements_by_class_name('ods-button--icon')
    i = 1
    while i < len(users):
        delete_users = users[i]
        delete_users.click()
        sleep(randint(2,5))
        actions = ActionChains(driver) 
        actions.send_keys(Keys.RETURN * 2)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(randint(2,5))
        if i >= 1:
            i += 1
        else:
            break

def reload_users():
    driver.navigate().refresh()
    driver.execute_script("window.scrollTo(0, 1000)")
    sleep(randint(2,5))

while (True):
    delete_loop()
    reload_users()