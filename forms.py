import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base_config import parse_config
from methods import generate_random_numbers, generate_random_string, concat_strings, centralize
from selenium.webdriver.common.keys import Keys

browser = parse_config()

def sort_elements():

    browser.get("https://demoqa.com/automation-practice-form")

    #wait = WebDriverWait(browser, 3)

    #forms_menu = browser.find_element(By.XPATH, "//h5[text()='Forms']")
    #forms_menu.click()

    #practice_form_submenu = browser.find_element(By.XPATH, "//span[text()='Practice Form']")
    #practice_form_submenu.click()

    first_name = browser.find_element(By.ID, "firstName")
    first_name.send_keys(generate_random_string(6))

    last_name = browser.find_element(By.ID, "lastName")
    last_name.send_keys(
        concat_strings(
            generate_random_string(5), generate_random_string(9)
        )
    )

    email = browser.find_element(By.ID, "userEmail")
    email.send_keys((generate_random_string(6) + '@' + generate_random_string(6) + '.com'))
    
    #random_radio = random.choice(['gender-radio-1', 'gender-radio-3', 'gender-radio-2'])
    gender_radios = browser.find_element(By.ID, "gender-radio-1")
    actions = ActionChains(browser)
    actions.click(gender_radios).perform()        

    mobile = browser.find_element(By.ID, "userNumber")
    mobile.send_keys(generate_random_numbers())

    centralize(browser, browser.find_element(By.ID, "userForm"), 450)
    time.sleep(3)

    birth_date = browser.find_element(By.ID, "dateOfBirthInput")
    actions = ActionChains(browser)
    actions.click(birth_date).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys('12/12/1990').send_keys(Keys.ENTER).perform()        

    Subjects_dropdown = browser.find_element(By.ID, "subjectsContainer")
    actions = ActionChains(browser)
    actions.click(Subjects_dropdown).send_keys('s').pause(1).send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform() 

    #random_checkbox = random.choice(['hobbies-checkbox-2', 'hobbies-checkbox-1', 'hobbies-checkbox-3'])
    hobbies_checkbox = browser.find_element(By.ID, "hobbies-checkbox-2")
    actions = ActionChains(browser)
    actions.click(hobbies_checkbox).perform()    

    file_input = browser.find_element(By.ID, "uploadPicture")
    file_input.send_keys('/home/macedo/desafio-accenture-selenium/arquivo.txt')

    currentAddress = browser.find_element(By.ID, "currentAddress")
    currentAddress.send_keys(
        concat_strings(
            generate_random_string(12), generate_random_string(9)
        )
    )
    currentAddress.send_keys(' ')
    currentAddress.send_keys(
        concat_strings(
            generate_random_string(5), generate_random_string(7)
        )
    )
    
    state = browser.find_element(By.ID, "state")
    actions = ActionChains(browser)
    actions.click(state).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    city = browser.find_element(By.ID, "city")
    actions = ActionChains(browser)
    actions.click(city).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    submit = browser.find_element(By.ID, "submit")
    submit.click()
    
    time.sleep(5)

    closeLargeModal = browser.find_element(By.ID, "closeLargeModal")
    closeLargeModal.click()
    
sort_elements()
