
# Necessary imports added ---

# Complete Assignment repo -->  https://github.com/codewithjaspreet/clootrack_assignment


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


        count = 3  # I am adding first 3 food items for testing to cart & display the discount price & other extra details for better understanding

        while(count > 0 ):

            for curbutton in add_buttons:

                if curbutton is not None:
                    curbutton.click()

                    driver.implicitly_wait(10)

                    item_add_button = WebDriverWait(driver,5).until(

                        EC.visibility_of_element_located((By.XPATH, "//button[@class='addCTA']"))
                    )

                   ## item_add_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='addCTA']")))
                                        
                    item_add_button.click()
                    print('Item added to cart')

                  

                    count -= 1


                    if count == 0:
                        break
        

        # Now we have added 5 items to cart -- we need to get the discount price & other addtional details I added

        driver.implicitly_wait(5)
        actual_price = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='highPrice']")))
        price_after_discount = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='finalPrice']")))
        total_items_added = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cartItemCount']")))
        total_savings = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='savingPrice']")))


       # CHECK CONSOLE FOR CALCULATED DATA -- I am printing the data to console 

        if actual_price is not None:
            print(f'Your total actual price is {actual_price.text} ')

        if price_after_discount is not None:
         print(f'Your total price to pay after discount is {price_after_discount.text}')   ### This is the discount price


        if total_items_added is not None:
             print(f'You have added {total_items_added.text} items to cart')

        if total_savings is not None:
            print (f'You have saved {total_savings.text}')

        data = {

            'Actual Price': [actual_price.text],
            'Discounted Price': [price_after_discount.text],
            'Items Added': [total_items_added.text.split(' ')[0]],
            'Savings': [total_savings.text]
        }

        df = pd.DataFrame(data)

        df.to_csv('discount_&_other_details.csv', index=False)

        print('Data has been saved to csv file in the same directory')

       

    

    except Exception as e:
        print(f'Error: {e.with_traceback}')
        import traceback
        traceback.print_exc()
        driver.quit()



if __name__ == "__main__":
    
    itemsToAdd()
    print('--------')
    print('\n')


    while True:
        pass

  