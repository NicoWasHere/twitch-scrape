#A python script to test if an account is banned on twitch.tv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager

#checks provided file before hand
if len(sys.argv)>1:
    if sys.argv[1] == "-h" or sys.argv[1] == "-help":
        print("Run this file in the command line with the path of a file you want to iterate through as an argument.\nYou can also use parse_file.py to make each line valid as a username. Use the -h command on it for more info\nusasge. python3 twitch_ban_checker.py [file path]")
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

#returns true if a there is an element with the tag_name in the given element
def check_exists_by_class_name(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True

def check_user(username):
    #opens twitch
    driver.get(f'https://www.twitch.tv/popout/{username}/chat?popout=')
    #waits until the page loads the answer
    while(not check_exists_by_class_name('chat-line__status')):
        pass
    #prints the response method form twitch
    ban_status = "suspended" in driver.find_element_by_class_name("chat-line__status").text
    return ban_status

#trys every word in a file
def use_file(file):
    words = open(file,'r')
    for word in words.readlines():
        #sanatizes words
        word = word.strip('\n')
        if(len(word) in range(4,25) and word.isalnum()):
            #tests words
            if(check_user(word)):
                banned.write(word+"\n")
            else:
                not_banned.write(word+"\n")
    words.close()



banned = open("banned.txt",'w')
not_banned = open("not_banned.txt",'w')
use_file(sys.argv[1])
banned.close()
not_banned.close()
driver.quit()



