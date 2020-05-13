from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time
import sys

#checks provided file before hand
if len(sys.argv)>1:
    if sys.argv[1] == "-h" or sys.argv[1] == "-help":
        print("Run this file in the command line with the path of a file you want to iterate through as an argument.\nYou can also use parse_file.py to make each line valid as a username. Use the -h command on it for more info\nusasge. python3 twitch_name_file.py [file path]")
        exit()
    try:
        open(sys.argv[1],'r').close()
    except:
        print("FILE NOT FOUND")
        exit()
else:
    print("FILE NOT FOUND")
    exit()

driver = webdriver.Chrome('./drivers/chromedriver') 

#returns true if a there is an element with the tag_name in the given element
def check_exists_by_tag_name(element, tag_name):
    try:
        element.find_element_by_tag_name(tag_name)
    except NoSuchElementException:
        return False
    return True

#returns true if a there is an element with the class_name in the given element
def check_exists_by_class_name(element, class_name):
    try:
        element.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True

#checks if the name is valid. Returns true if valid
def validateName(name): 
    form.find_element_by_id("signup-username").send_keys(name)
    #waits until the page loads the answer
    while(not check_exists_by_tag_name(form,'figure')):
        pass
    #checks if name is valid
    if(check_exists_by_class_name(form,"tw-svg__asset--success")):
        return True
    return False

#trys every word in a file
def useFile(file):
    f.write("==========NEW RUN USING "+file+"\n===============")
    words = open(file,'r')
    for word in words.readlines():
        word = word.strip('\n')
        if(len(word)>3 and word.isalnum()):
            if(validateName(word)):
                print(word)
                f.write(word+'\n')
            for x in word:
                form.find_element_by_id("signup-username").send_keys(Keys.BACK_SPACE)
    words.close()

#opens twitch
driver.get("https://www.twitch.tv/")
#delay to let the page load
time.sleep(3)
driver.find_element_by_tag_name('nav').find_elements_by_tag_name('button')[5].click()
time.sleep(3)
form = driver.find_element_by_tag_name('form')
f = open("results.txt","a")

if len(sys.argv)>1:
    try:
         useFile(sys.argv[1])
    except:
        print("FILE NOT FOUND")
driver.quit()
f.close()


