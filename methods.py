from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
import string
import random

def centralize(browser, iframe, value):
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(browser).scroll_from_origin(scroll_origin, 0, value).perform()

def generate_random_string(size=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))

def generate_random_numbers(size=10):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(size))

def concat_strings(string1, string2):
    return string1 + ' ' + string2