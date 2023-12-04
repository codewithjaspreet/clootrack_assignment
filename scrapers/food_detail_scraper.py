
# Necessary imports added ---
import csv
from selenium import webdriver
import requests
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to chromedriver from local machine -
chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")

# Starting browser & settings --
driver = webdriver.Chrome(options=chrome_options)
total_food_names = []
total_food_prices = []

def get_food_data():
    try:
        driver.get('https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/')

        food_types = ['Kulcha Burger', 'Chinese Fried Rice & Noodle Bowl', '3 Layer Rice Bowl', 'Indian Thalis', 'Breakfast And Snacks', 'Desserts & Juices']
       
        # Added explicit wait for the page to load completely
        wait = WebDriverWait(driver, timeout=10)

        wait.until(EC.presence_of_element_located((By.XPATH, "//header[@class='subListingsHeader']//p"))).click()
        

        for curfoodtype in food_types:



                food_names = []
                food_prices = []

                # Getting the food prices
                avaliable_meal_prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//article[@id ='{curfoodtype}']//div//section//div//article//p//span[@class='itemPrice']")))

                # Getting the food names
                avaliable_meal_names  = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//article[@id ='{curfoodtype}']//div//section//div//article//p[@class='itemName']")))

                # Print the food names
                if avaliable_meal_names:
                    food_names = [curfoodname.text for curfoodname in avaliable_meal_names]
                    total_food_names.extend(food_names)
                else:
                    print(f'No food names found for {curfoodtype}')

                # Print the food prices
                if avaliable_meal_prices:
                    food_prices = [curfoodprice.text for curfoodprice in avaliable_meal_prices]
                    total_food_prices.extend(food_prices)
                else:
                    print(f'No food prices found for {curfoodtype}')


               


    except Exception as e:
         print(f'{e} - error occurred while opening the website')
         driver.quit()

    
def make_csv(food_names, food_prices):
    df = pd.DataFrame(list(zip(food_names, food_prices)), columns=['Food Name', 'Food Price'])
    df.to_csv('food_data.csv', index=False)

if __name__ == "__main__":
    
    get_food_data()
    make_csv(total_food_names, total_food_prices)
    # Quit the WebDriver
    print('Done Scraping Data -- find the csv file in the same directory :)')
    
    while True:
        pass

