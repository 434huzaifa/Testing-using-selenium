from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from playsound import playsound
ser = Service(r"chromedriver.exe") #r for free charecter

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--enable-javascript")
#chrome_options.add_argument("--start-maximized")
driver=webdriver.Chrome(service=ser,options=chrome_options) # dont close the browser
ac=ActionChains(driver)
#driver=webdriver.Chrome(service=ser) # close the browser
driver.get("http://127.0.0.1:5000/")

def getSource():
     open('home.html','w').write(driver.page_source)


def login():
    driver.find_element(By.ID,"loginLabel").click()
    time.sleep(1)
    e=driver.find_element(By.ID,"user_email")
    e.send_keys("434.darkmaster@gmail.com")

    e=driver.find_element(By.ID,"user_password")
    e.send_keys("asd")

    driver.find_elements(By.TAG_NAME,"button")[1].click()
    time.sleep(1)
    try:
        driver.find_element(By.ID,"login_error")
        print("Login Failed")
        return False   
    except NoSuchElementException:
        print("Login Success")
        return True

def EnterCatrgory():
    try:
        cate_element=driver.find_elements(By.CLASS_NAME,'card-img-top')
        cate_element[0].click()
        return True
    except NoSuchElementException:
        print("There is no Category")
        return False

def T13():
    try:
        time.sleep(1)
        items=driver.find_elements(By.CLASS_NAME,'col-md-6')
        old_len=len(items)
    except NoSuchElementException:
        print("There is no item")
        return
    produc_img=items[0].find_element(By.CLASS_NAME,'product-image')
        
    ac.move_to_element(produc_img).perform()#hover
    produc_img.find_elements(By.CLASS_NAME,"btn")[1].click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"deletebtn").click()
    time.sleep(1)
    items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    time.sleep(1)
    new_len=0
    for i in items:
        dis=i.value_of_css_property('display')
        if dis!='none':
            new_len+=1
            
    if new_len<old_len:
        print("Delete One Item Success")
    else:
        print("Delete One Item Fail")

def T14():
    try:
        time.sleep(1)
        items=driver.find_elements(By.CLASS_NAME,'col-md-6')
        old_len=len(items)
    except NoSuchElementException:
        print("There is no item")
        return
    produc_img=items[0].find_element(By.CLASS_NAME,'product-image')
        
    ac.move_to_element(produc_img).perform()#hover
    produc_img.find_elements(By.CLASS_NAME,"btn")[1].click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"cancelbtn").click()
    time.sleep(1)
    items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    time.sleep(1)
    new_len=0
    for i in items:
        dis=i.value_of_css_property('display')
        if dis!='none':
            new_len+=1
            
    if new_len==old_len:
        print("Delete Cancel Success")
    else:
        print("Delete Cancel Fail")

def T15():
    new_title='w'
    try:
        time.sleep(1)
        items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    produc_img=items[0].find_element(By.CLASS_NAME,'product-image')
        
    ac.move_to_element(produc_img).perform()#hover
    produc_img.find_elements(By.CLASS_NAME,"btn")[0].click()
    time.sleep(1)
    
    title=driver.find_element(By.ID,'title')
    title.clear()
    title.send_keys(new_title)
    time.sleep(1)
    driver.find_elements(By.TAG_NAME,'button')[1].click()
    items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    if(items[0].find_element(By.TAG_NAME,'h1').get_attribute('innerHTML')==new_title):
        print('Title Change Success')
    else:
        print('Title Change Fail')

def T16():
    try:
        time.sleep(1)
        items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    produc_img=items[0].find_element(By.CLASS_NAME,'product-image')
        
    ac.move_to_element(produc_img).perform()#hover
    produc_img.find_elements(By.CLASS_NAME,"btn")[0].click()
    time.sleep(1)
    
    title=driver.find_element(By.ID,'title')
    title.clear()
    driver.find_element(By.ID,'about').clear()
    driver.find_element(By.ID,'link').clear()
    drop_down=Select(driver.find_element(By.ID,'item_type'))
    drop_down.select_by_visible_text('Select Item Type')
    time.sleep(1)
    driver.find_elements(By.TAG_NAME,'button')[1].click()
   
    
    try:
        title=driver.find_element(By.ID,'title')
        print('No update happend')
    except NoSuchElementException:
        print('updated happend')

def T17():
    try:
        time.sleep(1)
        items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    produc_img=items[0].find_element(By.CLASS_NAME,'product-image')
    ac.move_to_element(produc_img).perform()#hover
    produc_img.find_elements(By.CLASS_NAME,"btn")[0].click()
    time.sleep(1)
    image=driver.find_element(By.ID,'image')
    image.send_keys("C:\\Users\\Corrupted\\Pictures\\Untitled.png")
    driver.find_elements(By.TAG_NAME,'button')[1].click()
    try:
        title=driver.find_element(By.ID,'title')
        print('No update happend')
    except NoSuchElementException:
        print('updated happend')

def T18():
    try:
        time.sleep(1)
        items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    old_title=items[0].find_element(By.TAG_NAME,'h1').get_attribute('innerHTML')
    old_about=items[0].find_element(By.TAG_NAME,'p').get_attribute('innerHTML')
    old_link=items[0].find_element(By.TAG_NAME,'a').get_attribute('innerHTML')
    
    produc_img=items[0].find_element(By.CLASS_NAME,'product-image')
    ac.move_to_element(produc_img).perform()#hover
    produc_img.find_elements(By.CLASS_NAME,"btn")[0].click()
    title=driver.find_element(By.ID,'title')
    title.clear()
    title.send_keys('asda')
    about=driver.find_element(By.ID,'about')
    about.clear()
    about.send_keys('asdasda')
    link=driver.find_element(By.ID,'link')
    link.clear()
    link.send_keys('http://127.0.0.1:50000/')
    time.sleep(1)
    driver.find_elements(By.TAG_NAME,'button')[1].click()
    
    items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    new_title=items[0].find_element(By.TAG_NAME,'h1').get_attribute('innerHTML')
    new_about=items[0].find_element(By.TAG_NAME,'p').get_attribute('innerHTML')
    new_link=items[0].find_element(By.TAG_NAME,'a').get_attribute('innerHTML')
    
    if(old_title!=new_title):
        if old_about!=new_about:
            if old_link!=new_link:
                print('Update Success')
            else:
                print('No update happen')
        else:
            print('No update happen')
    else:
        print('No update happen')
    
def T19():
    try:
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    
    driver.find_element(By.ID,'search').send_keys('Naruto')
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,'btn1.btn-primary')[1].click()
    
    time.sleep(1)
    error=driver.find_element(By.ID,'search-error').get_attribute('innerHTML')
    if error !='':
        print("No data found")
        return

    items=driver.find_elements(By.CLASS_NAME,'col-md-6')
    for item in  items:
        title=item.find_element(By.TAG_NAME,'h1').get_attribute('innerHTML').lower()
        if title.find('naruto') ==-1:
            print('Search Contains False Resutl')
            return
    print('Search only contains True result')
        

def T20():
    try:
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    
    driver.find_element(By.ID,'search').send_keys('Naruto')
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,'btn1.btn-primary')[1].click()
    
    time.sleep(1)
    error=driver.find_element(By.ID,'search-error').get_attribute('innerHTML')
    if error !='':
        print("No data found")
        return
    else:
        driver.find_element(By.ID,'search').clear()

        try:
            time.sleep(1)
            driver.find_elements(By.CLASS_NAME,'col-md-6')
            print("There is item")
            return 
        except NoSuchElementException:
            print("There is no item")
            return
        
        
def T21():
    try:
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME,'col-md-6')
    except NoSuchElementException:
        print("There is no item")
        return
    
    driver.find_element(By.ID,'search').send_keys('Naruto')
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,'btn1.btn-primary')[1].click()
    
    time.sleep(1)
    error=driver.find_element(By.ID,'search-error').get_attribute('innerHTML')
    if error !='':
        print("No data found")
        return
    else:
        search=driver.find_element(By.ID,'search')
        search.clear()
        search.send_keys('Tokyo')
        driver.find_elements(By.CLASS_NAME,'btn1.btn-primary')[1].click()
        try:
            time.sleep(1)
            items=driver.find_elements(By.CLASS_NAME,'col-md-6')
            
            for item in items:
                title=item.find_element(By.TAG_NAME,'h1').get_attribute('innerHTML').lower()
                if title.find('tokyo') ==-1:
                    print('Search Contains False Resutl')
                    return
            print('Search Contains True Resutl')
        except NoSuchElementException:
            print("item didnt show up")
            return
    
def T22():
    driver.find_element(By.CLASS_NAME,'btn1.btn-primary').click()
    time.sleep(1)
    try:
        driver.find_element(By.ID,'username')
        print('Logout successfull')
    except NoSuchElementException:
        print('Logout Failed')
def T23():
    driver.find_element(By.CLASS_NAME,'user').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,'btn4.btn-primary').click()
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.ID,"loginLabel").click()
    
    time.sleep(1)
    e=driver.find_element(By.ID,"user_email")
    e.send_keys("434.darkmaster@gmail.com")

    e=driver.find_element(By.ID,"user_password")
    e.send_keys("asd")

    driver.find_elements(By.TAG_NAME,"button")[1].click()
    time.sleep(1)
    try:
        driver.find_element(By.ID,"login_error")
        print("Account Deleted")

    except NoSuchElementException:
        print("Account Not Deleted")

def why():
    driver.execute_script('window.location="/"')
    EnterCatrgory()

if login():
    why()
    print('T13- ',end='')
    T13()
    why()
    print('T14- ',end='')
    T14()
    why()
    print('T15- ',end='')
    T15()
    why()
    print('T16- ',end='')
    T16()
    why()
    print('T17- ',end='')
    T17()
    why()
    print('T18- ',end='')
    T18()
    why()
    print('T19- ',end='')
    T19()
    why()
    print('T20- ',end='')
    T20()
    why()
    print('T21- ',end='')
    T21()
    print('T22- ',end='')
    T22()
    login()
    print('T23- ',end='')
    T23()
