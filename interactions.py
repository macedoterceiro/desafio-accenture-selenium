import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base_config import parse_config
from methods import centralize

browser = parse_config()
    
def sort_elements():

    browser.get("https://demoqa.com/")

    wait = WebDriverWait(browser, 3)

    interactions_menu = browser.find_element(By.XPATH, "//h5[text()='Interactions']")
    interactions_menu.click()

    sortable_submenu = browser.find_element(By.XPATH, "//span[text()='Sortable']")
    sortable_submenu.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='demo-tabpane-list']")))

    time.sleep(3)

    centralize(browser, browser.find_element(By.XPATH, "//div[contains(@class,'sortable-container')]"), 300)

    items = browser.find_elements(By.XPATH, "//div[contains(@class,'list-group-item')]")
    items_list = [item.text for item in items]
    items_list = [item for item in items_list if item != '']

    time.sleep(3)

    items_list.reverse()
        
    for i in range(len(items_list)-1):
        item = browser.find_element(By.XPATH, f"//div[contains(@class,'list-group-item')][text()='{items_list[i]}']")
        actions = ActionChains(browser)
        actions.drag_and_drop(item, items[i]).perform()           

    time.sleep(5)
    browser.quit()

sort_elements()
