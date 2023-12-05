
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
driver = webdriver.Chrome(options=chrome_options)




def itemsToAdd():

    try:
        driver.get('https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/')
        
        wait = WebDriverWait(driver, 5)

        add_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='countCta add ']")))


        count = 5  # I am adding first 5 food items for testing to cart & display the discount price

        while(count > 0 ):

            for curbutton in add_buttons:

                if curbutton is not None:
                    curbutton.click()

                    driver.implicitly_wait(2)
                    item_add_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='addCTA']")))
                    item_add_button.click()

                    print(f'Added {count} items to cart')


                    count -= 1


                    if count == 0:
                        break
        

        # Now we have added 5 items to cart -- we need to get the discount price

        print("Yaha tk agya code")
        # driver.implicitly_wait(5)

        actual_price = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='highPrice']")))
        discount_price = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='finalPrice']")))
        total_items_added = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cartItemCount']")))

        total_savings = {actual_price.text} - {discount_price.text}

        print("code reached till calculations")

        if actual_price is not None:
            print(f'Your total actual price is {actual_price.text}')

        if discount_price is not None:
         print(f'Your total discount price is {discount_price.text}')   ### This is the discount price


        if total_items_added is not None:
             print(f'You have added {total_items_added.text} items to cart')

        if total_savings is not None:
            print (f'You have saved ₹{total_savings}')
    

    

    except Exception as e:
        print(f'Error: {e}')
        import traceback
        traceback.print_exc()
        driver.quit()




    



if __name__ == "__main__":
    

    # I am making a list of food that you can query for to add to cart -- this is for testing purposes
    # I am adding first 5 food items to cart & display the discount price 

    
    itemsToAdd()
    print('--------')
    print('\n')

   # print('Done Scraping Data -- find the csv file in the same directory :)')
    
