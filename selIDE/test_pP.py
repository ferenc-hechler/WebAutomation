# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPP():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pP(self):
    # Test name: PP
    # Step # | name | target | value
    # 1 | click | linkText=Aktivitäten | 
    self.driver.find_element(By.LINK_TEXT, "Aktivitäten").click()
    # 2 | click | id=filters-endDate | 
    self.driver.find_element(By.ID, "filters-endDate").click()
    # 3 | click | linkText=Letztes Jahr | 
    self.driver.find_element(By.LINK_TEXT, "Letztes Jahr").click()
    # 4 | click | id=freeTextSearch | 
    self.driver.find_element(By.ID, "freeTextSearch").click()
    # 5 | type | id=freeTextSearch | book
    self.driver.find_element(By.ID, "freeTextSearch").send_keys("book")
    # 6 | click | css=.ppvx_icon-search | 
    self.driver.find_element(By.CSS_SELECTOR, ".ppvx_icon-search").click()
    # 7 | storeText | css=#txnDescription-6KK70434TJ2614929 .netAmount | cost1
    self.vars["cost1"] = self.driver.find_element(By.CSS_SELECTOR, "#txnDescription-6KK70434TJ2614929 .netAmount").text
    # 8 | storeText | css=#txnDescription-2SE51564YG634105L .netAmount | cost2
    self.vars["cost2"] = self.driver.find_element(By.CSS_SELECTOR, "#txnDescription-2SE51564YG634105L .netAmount").text
    # 9 | click | css=.transactionRow:nth-child(1) .ppvx_icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".transactionRow:nth-child(1) .ppvx_icon").click()
    # 10 | click | css=.ppvx_col-4 > .primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".ppvx_col-4 > .primary").click()
    # 11 | storeText | css=.ppvx_col-4 > .primary | cost1b
    self.vars["cost1b"] = self.driver.find_element(By.CSS_SELECTOR, ".ppvx_col-4 > .primary").text
    # 12 | click | css=.transactionRow:nth-child(2) .ppvx_icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".transactionRow:nth-child(2) .ppvx_icon").click()
    # 13 | click | css=#transactionDetails-2SE51564YG634105L .purchaseDetailFields .ppvx_col-4 | 
    self.driver.find_element(By.CSS_SELECTOR, "#transactionDetails-2SE51564YG634105L .purchaseDetailFields .ppvx_col-4").click()
    # 14 | storeText | css=#transactionDetails-2SE51564YG634105L .ppvx_col-4:nth-child(2) > .primary:nth-child(1) | c2b
    self.vars["c2b"] = self.driver.find_element(By.CSS_SELECTOR, "#transactionDetails-2SE51564YG634105L .ppvx_col-4:nth-child(2) > .primary:nth-child(1)").text
    # 15 | click | css=.transactionRow:nth-child(8) .ppvx_icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".transactionRow:nth-child(8) .ppvx_icon").click()
    # 16 | storeText | css=#txnDescription-10X281899U702240E > #txnDate-10X281899U702240E | date
    self.vars["date"] = self.driver.find_element(By.CSS_SELECTOR, "#txnDescription-10X281899U702240E > #txnDate-10X281899U702240E").text
    # 17 | click | id=txnDescription-10X281899U702240E | 
    self.driver.find_element(By.ID, "txnDescription-10X281899U702240E").click()
    # 18 | storeText | css=#txnDescription-10X281899U702240E > #txnDate-10X281899U702240E | lastDate
    self.vars["lastDate"] = self.driver.find_element(By.CSS_SELECTOR, "#txnDescription-10X281899U702240E > #txnDate-10X281899U702240E").text
    # 19 | click | id=filters-endDate | 
    self.driver.find_element(By.ID, "filters-endDate").click()
    # 20 | click | id=filters-endDate | 
    self.driver.find_element(By.ID, "filters-endDate").click()
    # 21 | click | id=filters-endDate | 
    self.driver.find_element(By.ID, "filters-endDate").click()
    # 22 | type | id=filters-endDate | 03.10.2020
    self.driver.find_element(By.ID, "filters-endDate").send_keys("03.10.2020")
    # 23 | sendKeys | id=filters-endDate | ${KEY_ENTER}
    self.driver.find_element(By.ID, "filters-endDate").send_keys(Keys.ENTER)
    # 24 | click | id=filters-endDate | 
    self.driver.find_element(By.ID, "filters-endDate").click()
    # 25 | click | id=filters-endDate | 
    self.driver.find_element(By.ID, "filters-endDate").click()
    # 26 | type | id=filters-endDate | 03.10.20
    self.driver.find_element(By.ID, "filters-endDate").send_keys("03.10.20")
    # 27 | sendKeys | id=filters-endDate | ${KEY_ENTER}
    self.driver.find_element(By.ID, "filters-endDate").send_keys(Keys.ENTER)
  
