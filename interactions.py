import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base_config import parse_config
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

browser = parse_config()

def centralize(iframe):
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(browser).scroll_from_origin(scroll_origin, 0, 300).perform()
    
def sort_elements():

    browser.get("https://demoqa.com/")

    wait = WebDriverWait(browser, 3)

    interactions_menu = browser.find_element(By.XPATH, "//h5[text()='Interactions']")
    interactions_menu.click()

    sortable_submenu = browser.find_element(By.XPATH, "//span[text()='Sortable']")
    sortable_submenu.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='demo-tabpane-list']")))

    centralize(browser.find_element(By.XPATH, "//div[@id='Ad.Plus-970x250-1']"))

    items = browser.find_elements(By.XPATH, "//div[contains(@class,'list-group-item')]")
    items_list = [item.text for item in items]
    items_list = [item for item in items_list if item != '']

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='Ad.Plus-970x250-1']")))

    # Reverse list
    items_list.reverse()
    
    for i in range(len(items_list)-1):
        item = browser.find_element(By.XPATH, f"//div[contains(@class,'list-group-item')][text()='{items_list[i]}']")
        actions = ActionChains(browser)
        actions.send_keys('Space').drag_and_drop(item, items[i]).perform()        

    # Fechar o navegador
    time.sleep(10)
    browser.quit()

# Executar o script
sort_elements()
