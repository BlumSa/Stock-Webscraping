from selenium import webdriver
from pynput.keyboard import Key, Controller
import csv
import time

keyboard = Controller()

#DONT LOAD PICTURES (FOR SPEED)
chrome_options=webdriver.ChromeOptions()
prefs={"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs", prefs)

#LINK TO CHROMEDRIVER AND LOAD WEBSITE
browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
browser.get('https://www.tdameritrade.com')

#USERNAME
xpath = '//*[@id="userid"]'
element = browser.find_element_by_xpath(xpath)
element.send_keys('')
time.sleep(2)

#PASSWORD
xpath = '//*[@id="password"]'
element = browser.find_element_by_xpath(xpath)
element.send_keys('')
time.sleep(2)

#CLICK TO LOGIN
xpath = '//*[@id="form-login"]/div[1]/button'
element = browser.find_element_by_xpath(xpath)
element.click()
time.sleep(3)

def security():
#SECURITY QUESTIONS
   answer = 'challengeAnswer'
   answer = browser.find_element_by_name(answer)
   answer.click()
   answer.click()
   question = '//*[@id="loginBlock"]/div[1]/p[2]'
   question = browser.find_element_by_xpath(question).text

   if question == "Question: What was the name of your junior high school? (Enter only 'Dell' for Dell Junior High School.)":
      answer.send_keys('')
      submit = '//*[contains(@id,"securityChallenge_label")]'
      submit = browser.find_element_by_xpath(submit)
      submit.click()

   elif question == "Question: In what city were you born? (Enter full name of city only.)":
      answer.send_keys('')
      answer.click()
      submit = '//*[contains(@id,"securityChallenge_label")]'
      submit = browser.find_element_by_xpath(submit)
      submit.click()

   elif question == "Question: What is your best friend's first name?":
      answer.send_keys('')
      answer.click()
      submit = '//*[contains(@id,"securityChallenge_label")]'
      submit = browser.find_element_by_xpath(submit)
      submit.click()

   elif question == "Question: What is your father's middle name?":
      answer.send_keys('')
      answer.click()
      submit = '//*[contains(@id,"securityChallenge_label")]'
      submit = browser.find_element_by_xpath(submit)
      submit.click()

   return browser    

security()

#READ TICKER FROM CSV
file = open('tickers.txt', 'r')
ticker = file.readline()
ticker = str(ticker)
print(ticker)

#OUTPUT BALANCE TO CSV
xpath = '//*[@id="tda_module_Balances_BalancesAndPositions_0"]/div[4]/div[1]/div/div[1]/span[2]/span[1]'
element = browser.find_element_by_xpath(xpath).text
element = str(element)
file = open('scottrade.csv', 'a')
file.write('\n' + element)
file.close()

#SEACH TICKER STOCK PRICE
xpath = '//*[@id="siteSearch"]'
element = browser.find_element_by_xpath(xpath)
element.send_keys(ticker)
xpath = '//*[@id="searchIcon"]'
element = browser.find_element_by_xpath(xpath)
element.click()
time.sleep(2)

#OUTPUT TICKER STOCK PRICE
#xpath = 'quote.dataGroup'
#element = browser.find_element_by_class_name(xpath)
#element.click()
#print(element)

#SWITCH BACK TO DEFAULT CHROME SETTINGS AND LOG OFF
browser.switch_to.default_content()
logoff = browser.find_element_by_link_text('Log Out')
logoff.click()
browser.close()
browser.quit()
