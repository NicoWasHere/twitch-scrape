from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager

#all of the characters allowed in a twitch username
valid_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']

if len(sys.argv)>1 and sys.argv[1] == "-h" or sys.argv[1] == "-help":
    print("Run this file in the command line to iterate all possible letter combinations.\nYou can specify a starting point for the file to interate from or the number of characters in each combonation.\nusasge. python3 twitch_name_combinations.py [starting word (optional)] [number (optional)]")
    exit()

#can be replaced with the location of the chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

#repersents the name. Can choose any starting name but entering the right indexes. Can also choose length by length of array
nameCode = [0,0,0,0,0,0]

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

#changes nameCode to the next name
def iterateName():
    global nameCode
    n = len(nameCode)-1
    while nameCode[n]==34:
        nameCode[n] = 0
        n-=1
    nameCode[n]+=1

#checks to make sure it won't go out of bounds
def checkNotFin():
    global nameCode
    for code in nameCode:
        if code !=34:
            return True
    return False

#checks if the name is valid. Returns true if valid
def validateName(name): 
    form.find_element_by_id("signup-username").send_keys(name)
    #waits until the page loads the answer
    while(not check_exists_by_tag_name(form,'figure')):
        pass
    #checks if name is valid
    if(check_exists_by_class_name(form,"kJKagf")):
        return True
    return False

#runs through every combination of names using name code
def combinations():
    global nameCode
    f.write("==========NEW RUN STARTING AT "+str(nameCode)+"\n===============")
    while checkNotFin():
        name = ""
        for code in nameCode:
            name += str(valid_chars[code])
        if(validateName(name)):
            print(name)
            f.write(name+'\n')
        #clears form
        for x in name:
            form.find_element_by_id("signup-username").send_keys(Keys.BACK_SPACE)
        iterateName()

def setCode(name):
    global nameCode
    nameCode = []
    for letter in name:
        if(not letter.isalnum()):
            print("ERROR INVALID CHARACTERS ENTERED")
            driver.close()
            exit()
        nameCode.append(int(str(ord(letter.lower())-97)))

#opens twitch
driver.get("https://www.twitch.tv/")
#delay to let the page load
time.sleep(3)
driver.find_element_by_tag_name('nav').find_elements_by_tag_name('button')[5].click()
time.sleep(3)
form = driver.find_element_by_tag_name('form')
if len(sys.argv)>1:
    if sys.argv[1].isnumeric():
        nameCode = []
        for x in range(int(sys.argv[1])):
            nameCode.append(0)
    else:
        setCode(sys.argv[1])

f = open(sys.argv[0].split("twitch_name")[0]+"results.txt","a")
combinations()
driver.quit()
f.close()


