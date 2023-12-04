
# Neccessary imports added ---
import csv
import selenium
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



#Path to chromedriver from localmachine - 
chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized") 

# starting browser & settings --
driver = webdriver.Chrome( options=chrome_options)





def get_food_data(curfoodtype):
    

    try:
        driver.get('https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/')


        # added a explicit wait for the page to load completely
        wait = WebDriverWait(driver, timeout=2)


        # getting the food prices
        avaliable_meal_prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//article[@id ='{curfoodtype}']//div//section//div//article//p//span[@class='itemPrice']")))

        # getting the food names
        avaliable_meal_names  = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//article[@id ='{curfoodtype}']//div//section//div//article//p[@class='itemName']")))
       
        # print the food names
        if avaliable_meal_names is not None:

            for curfoodname in avaliable_meal_names:
                print(curfoodname.text)
        
        else:

            print(f'No food names found for {curfoodtype}')

        
        # print the food prices

        if avaliable_meal_prices is not None:

            for curfoodprice in avaliable_meal_prices:
                print(curfoodprice.text)
        
        else:

            print(f'No food prices found for {curfoodtype}')
        

    

    except Exception as e:
        print(f'{e} - error occured while opening the website')
        driver.quit()


def data_processing():
    pass


def make_csv():
    pass




if __name__ == "__main__":

    food_types = ['Kulcha Burger' , 'Chinese Fried Rice & Noodle Bowl' , '3 Layer Rice Bowl' , 'Fruit Pop' , 'Indian Thalis' , 'Gourmet By EatFit' , 'Breakfast And Snacks' , 'Healthy Khichdi' , 'A La Carte' , 'Desserts & Juices']

    # for curfoodtype in food_types:
    #     get_food_data(curfoodtype)

    get_food_data('Kulcha Burger')

    while True:
        pass

