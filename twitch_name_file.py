#A python script to test for avaliable usernames on twitch.tv using a browser based exploit to avoid rate limiting

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager

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

#installs the chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

#gets the class name of the fail icon
def check_username_available():
    svg = form.find_elements_by_tag_name("svg")[0]
    return svg.get_attribute("type") == "color-fill-success"

#returns true if a there is an element with the tag_name in the given element
def check_exists_by_tag_name(element, tag_name):
    try:
        element.find_element_by_tag_name(tag_name)
    except NoSuchElementException:
        return False
    return True


#checks if the name is valid. Returns true if valid
def validate_name(name): 
    form.find_element_by_id("signup-username").send_keys(name)
    #waits until the page loads the answer
    while(not check_exists_by_tag_name(form,'figure')):
        pass
    #checks if name is valid
    return check_username_available()

#trys every word in a file
def use_file(file):
    f.write("==========NEW RUN USING "+file+"===============\n")
    words = open(file,'r')
    for word in words.readlines():
        #sanatizes words
        word = word.strip('\n')
        if(len(word)>3 and word.isalnum()):
            #tests words
            if(validate_name(word)):
                print(word)
                f.write(word+'\n')
            #clears the form
            for x in word:
                form.find_element_by_id("signup-username").send_keys(Keys.BACK_SPACE)
    words.close()

#opens twitch
driver.get("https://www.twitch.tv/")
#delay to let the page load
time.sleep(3)
driver.find_element_by_tag_name('nav').find_elements_by_tag_name('button')[5].click()
form = driver.find_element_by_tag_name('form')
f = open("results.txt","a")

if len(sys.argv)>1:
    try:
         use_file(sys.argv[1])
    except:
        print("FILE NOT FOUND")
driver.quit()
f.close()


