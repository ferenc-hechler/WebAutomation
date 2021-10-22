from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HumbleBundle:

    def __init__(self, driver):
        self.driver:webdriver = driver

    def css_selector(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def css_selector_text(self, selector):
        return self.css_selector(selector).text
    
    def selectEinkaeufe(self):
        self.driver.get("https://www.humblebundle.com/home/purchases?hmb_source=navbar")
        #self.driver.find_element(By.CSS_SELECTOR, ".navbar-item > img").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".secondary-caret").click()
        #self.driver.find_element(By.LINK_TEXT, "Einkäufe").click()

    def filter_einkaeufe(self, filter):
        self.driver.find_element(By.ID, "purchase-search").send_keys(filter)

    def get_item(self, n):
        return [self.css_selector_text(f".row:nth-child({n}) > .product-name"), 
                self.css_selector_text(f".row:nth-child({n}) > .order-placed"), 
                self.css_selector_text(f".row:nth-child({n}) > .total")
            ]
        
    def get_count_items(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, f".row")
        return len(items)
        
    def next_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".js-pagination-holder:nth-child(2) .hb-chevron-right").click()

    def has_next_page(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".js-pagination-holder:nth-child(2) .hb-chevron-right")
            return True
        except NoSuchElementException:
            return False

    def prev_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".js-pagination-holder:nth-child(2) .hb-chevron-left").click()
        

    def xp(self, xpath):
        "Return the DOM element of the xpath or 'None' if the element is not found "
        try:
            return self.driver.find_element(xpath)
        except Exception:
            return None
