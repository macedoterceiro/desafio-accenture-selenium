import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from base_config import parse_config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from methods import generate_random_numbers, generate_random_string, concat_strings, centralize

browser = parse_config()
    
def fill_form():
    time.sleep(1)

    first_name = browser.find_element(By.ID, "firstName")
    actions = ActionChains(browser)
    actions.click(first_name).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(generate_random_string(6)).perform()

    last_name = browser.find_element(By.ID, "lastName")
    actions = ActionChains(browser)
    actions.click(last_name).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
        concat_strings(
            generate_random_string(5), generate_random_string(9)
        )
    ).perform()

    email = browser.find_element(By.ID, "userEmail")
    actions = ActionChains(browser)
    actions.click(email).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
        (generate_random_string(6) + '@' + generate_random_string(6) + '.com')
    ).perform()

    age = browser.find_element(By.ID, "age")
    actions = ActionChains(browser)
    actions.click(age).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(generate_random_numbers(2)).perform()

    salary = browser.find_element(By.ID, "salary")
    actions = ActionChains(browser)
    actions.click(salary).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(generate_random_numbers(4)).perform()

    department = browser.find_element(By.ID, "department")
    actions = ActionChains(browser)
    actions.click(department).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(generate_random_string(8)).perform()

    time.sleep(3)

    submit = browser.find_element(By.ID, "submit")
    submit.click()

    time.sleep(3)

def sort_elements():

    browser.get("https://demoqa.com/")

    wait = WebDriverWait(browser, 3)

    elements_menu = browser.find_element(By.XPATH, "//h5[text()='Elements']")
    elements_menu.click()

    web_tables_submenu = browser.find_element(By.XPATH, "//span[text()='Web Tables']")
    web_tables_submenu.click()

    add_record = browser.find_element(By.ID, "addNewRecordButton")
    add_record.click()

    fill_form()

    centralize(browser, browser.find_element(By.XPATH, "//div[contains(@class,'web-tables-wrapper')]"), 200, 0)
    centralize(browser, browser.find_element(By.XPATH, "//div[contains(@class,'web-tables-wrapper')]"), 0, 200)

    edit_records = browser.find_elements(By.CSS_SELECTOR, "[id*='edit-record']")
    actions = ActionChains(browser)
    actions.click(edit_records[-1]).perform()

    fill_form()

    delete_records = browser.find_elements(By.CSS_SELECTOR, "[id*='delete-record']")
    actions = ActionChains(browser)
    actions.click(delete_records[-1]).perform()

    time.sleep(10)
    browser.quit()

sort_elements()
