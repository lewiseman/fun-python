from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get('https://orteil.dashnet.org/cookieclicker/')

#wait for 5 sec before continuing
browser.implicitly_wait(5)

cookie = browser.find_element_by_id("bigCookie")
cookie_count = browser.find_element_by_id("cookies")

items = [browser.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(browser)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(browser)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()