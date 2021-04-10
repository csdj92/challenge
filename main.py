from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


def enter_username(user_browser):
    username = user_browser.find_element_by_id("username") # will throw exception if not found
    username.clear() #clear username in event there is prepopulated data
    username.send_keys("test") #send username
    print('Entered username')


def enter_password(pw_browser):
    password = pw_browser.find_element_by_id("password")
    password.clear() #clear password in event there is prepopulated data
    password.send_keys("test")  #send password  
   
    print('Entered password') 


    
def login(login_browser):
    login_button = login_browser.find_elements_by_xpath("//input[@type='submit' and @value='Login']")[0]
    login_button.click()
    print('Logged in')


def get_table_html(table_browser,force_exception):
    print('forcing exception', force_exception)
    if force_exception:
        tables = table_browser.find_elements_by_id('the_table') #Should throw an exception
    else:
        tables = table_browser.find_elements_by_id('the-table')
        print('Tables',tables)
    if not tables:
        raise NoSuchElementException("No tables found")
    
    table = tables[1]
    print('Table found and rows exist')
    return table.get_attribute('outerHTML')



def create_data_frame(table_html):
    webtable_df = pd.read_html(table_html)[0]
    print(table_html)
    print('Created dataframe')
    return webtable_df



def save_to_csv(data_frame):
    data_frame.to_csv(r'C:\Users\csdj9\OneDrive\Desktop\Data1.csv')
    print(data_frame)
    print('saved data')


#def download_data(data_browser,force_exception):
    data_browser.get("http://www.montmere.com/test.php")
    enter_username(data_browser)
    enter_password(data_browser)
    login(data_browser)
    time.sleep(5) # wait out spinner
    table_html =get_table_html(data_browser,force_exception)
    webtable_df = create_data_frame(table_html)
    save_to_csv(webtable_df)


browser = webdriver.Chrome() #start Chrome 

try:
    download_data(browser,True)
except NoSuchElementException as exception:
    print("Error has occurred")
    browser.delete_all_cookies()
    download_data(browser, False)
finally:
    browser.close()















browser = webdriver.Chrome() #Start Chrome

browser.get("http://www.montmere.com/test.php") #Get url

        
password = browser.find_element_by_id("password")#find css ID Password
password.clear() #clear password
password.send_keys("test")  #send password  
browser.find_elements_by_xpath("//input[@type='submit' and @value='Login']")[0].click() # Click login    

time.sleep(3) #Wait for table to load just incase script runs to fast

table = browser.find_elements_by_id('the-table')[1] #Get correct table
 
webtable_df = pd.read_html(table.find_element_by_xpath('//*[@id="the-table" and @class="table"]').get_attribute('outerHTML'))[0]  #find all inside table

webtable_df.to_csv(r'/Data1.csv') #Write to csv
