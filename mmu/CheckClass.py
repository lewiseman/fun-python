from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
browser.get('https://elearning.mmu.ac.ke/login/index.php')

#print the title
print(browser.title)

#credentials to login
username = "REG NUMBER"
password = "*********"

#input areas
NameInput = browser.find_element_by_id("username")
PassInput = browser.find_element_by_id("password")
LoginBtn = browser.find_element_by_id("loginbtn")

#actions to perform
NameInput.send_keys(username)
PassInput.send_keys(password)
time.sleep(1)
LoginBtn.click()


def unitfinder(unit):
    time.sleep(1)
    unit.click()
    time.sleep(1)

def channelfinder(channel):
    time.sleep(2)
    channel.click()

def gohome():
    time.sleep(2)
    browser.back()
    time.sleep(1)
    browser.back()

def gonext():
    nextpage = browser.find_element_by_link_text("2")
    time.sleep(1)
    nextpage.click()



#physics
physicsUnit = browser.find_element_by_link_text("PHYSICS")
unitfinder(physicsUnit)
physicsChannel = browser.find_element_by_xpath("//span[contains(text(), 'SPH 2172 Physics')]")
channelfinder(physicsChannel)  
time.sleep(1)
gohome()

#DISCRETE MATHEMATICS
discmathsunit = browser.find_element_by_link_text("DISCRETE MATHEMATICS")
unitfinder(discmathsunit)
discmathsChannel = browser.find_element_by_xpath("//span[contains(text(), 'INTRODUCTION TO SETS')]")
channelfinder(discmathsChannel)  
gohome()

#Mathematics for Science Yr1 Class of 2020
mathsforscience = browser.find_element_by_link_text("Mathematics for Science Yr1 Class of 2020")
unitfinder(mathsforscience)
mathsforscienceChannel = browser.find_element_by_xpath("//span[contains(text(), 'Mathematics for Science Yr 1 Class of 2020')]")
channelfinder(mathsforscienceChannel)  
gohome()


#Communication Skills
commskills = browser.find_element_by_link_text("Communication Skills")
unitfinder(commskills)
commskillsChannel = browser.find_element_by_xpath("//span[contains(text(), 'Comm.Skills- Introduction')]")
channelfinder(commskillsChannel)  
gohome()

#HIV/AIDS
hivaids = browser.find_element_by_link_text("HIV/AIDS")
unitfinder(hivaids)
hivaidsChannel = browser.find_element_by_xpath("//span[contains(text(), 'Virtual Classroom_1')]")
channelfinder(hivaidsChannel)  
gohome()

#Mathematics for Science
maoforscience = browser.find_element_by_link_text("Mathematics for Science")
unitfinder(maoforscience)
maoforscienceChannel = browser.find_element_by_xpath("//span[contains(text(), 'Mathematics for Science Yr 1 Class of 2020')]")
channelfinder(maoforscienceChannel)  
gohome()
gonext()

#Calculus I (MCS)
calcone = browser.find_element_by_link_text("Calculus I (MCS)")
unitfinder(calcone)
calconeChannel = browser.find_element_by_xpath("//span[contains(text(), 'Calculus 1 - SMA 2101/MAT 2101/MAT 2112/MTE 2116')]")
channelfinder(calconeChannel)  
gohome()
gonext()

#Discrete Mathematics
discmao = browser.find_element_by_link_text("Discrete Mathematics")
unitfinder(discmao)
discmaoChannel = browser.find_element_by_xpath("//span[contains(text(), 'Announcements')]")
channelfinder(discmaoChannel)  
gohome()
gonext()

#Physics
phyicunit = browser.find_element_by_link_text("Physics")
unitfinder(phyicunit)
phyicunitChannel = browser.find_element_by_xpath("//span[contains(text(), 'PHY 2172 Physics Virtual Classroom')]")
channelfinder(phyicunitChannel)  
gohome()
gonext()

#Calculus I (AC & IC)
acdc = browser.find_element_by_link_text("Calculus I (AC & IC)")
unitfinder(acdc)
acdcChannel = browser.find_element_by_xpath("//span[contains(text(), 'Virtual Classroom')]")
channelfinder(acdcChannel)  
gohome()
gonext()

#Computer Organization
comporg = browser.find_element_by_link_text("Computer Organization")
unitfinder(comporg)
comporgChannel = browser.find_element_by_xpath("//span[contains(text(), 'Computer Organization')]")
channelfinder(comporgChannel)  
gohome()
gonext()

#Introduction to Computer Systems
ics = browser.find_element_by_link_text("Introduction to Computer Systems")
unitfinder(ics)
icsChannel = browser.find_element_by_xpath("//span[contains(text(), 'First Meeting')]")
channelfinder(icsChannel)  
gohome()


#End
time.sleep(5)
browser.quit()
