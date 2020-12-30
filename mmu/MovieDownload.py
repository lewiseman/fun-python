from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://watchsomuch.org/')
print(browser.title)

time.sleep(3)

checkbox1 = browser.find_element_by_id("chkAgreement1")
checkbox2 = browser.find_element_by_id("chkAgreement2")
checkbox3 = browser.find_element_by_id("chkAgreement3")
checkbox4 = browser.find_element_by_id("chkAgreement4")
checkbox5 = browser.find_element_by_id("chkAgreement5")
btn = browser.find_element_by_id("btnIAgree")

#click on them
checkbox1.click()
checkbox2.click()
checkbox3.click()
checkbox4.click()
checkbox5.click()
btn.click()


search = browser.find_element_by_id("txtSearch")

title = input("what do you what do you want to search for:")

search.send_keys(title)

time.sleep(3)
#search.send_keys(Keys.RETURN)

# examples = browser.find_element_by_id("SearchSuggestions")
# links = [examples.find_element_by_tag_name("a")]
# for link in links:
#     #link = link.find_element_by_tag_name("a")
#     picked = link
#     picked.click()

# time.sleep(3)
# showtorrents = browser.find_element_by_id("btnShowTorrents")
# showtorrents.click()



main = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "SearchSuggestions"))
)
articles = main.find_elements_by_tag_name("a")
for article in articles:
    # header = article.find_element_by_class_name("title")
    # pick = header.text.splitlines()
    print(article.text)

pick = input("pick one :")
picked = browser.find_elements_by_tag_name("a:nth-child(" + pick + ")")


picked.click()
browser.quit()