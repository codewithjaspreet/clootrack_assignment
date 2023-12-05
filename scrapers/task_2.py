
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

                  

                    count -= 1


                    if count == 0:
                        break
        

        # Now we have added 5 items to cart -- we need to get the discount price & other addtional details I added

        # driver.implicitly_wait(5)

        actual_price = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='highPrice']")))
        price_after_discount = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='finalPrice']")))
        total_items_added = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cartItemCount']")))
        total_savings = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='savingPrice']")))


       # CHECK CONSOLE FOR CALCULATED DATA -- I am printing the data to console 

        if actual_price is not None:
            print(f'Your total actual price is {actual_price.text}')

        if price_after_discount is not None:
         print(f'Your total price to pay after discount is {price_after_discount.text}')   ### This is the discount price


        if total_items_added is not None:
             print(f'You have added {total_items_added.text} items to cart')

        if total_savings is not None:
            print (f'You have saved {total_savings.text}')
    

    

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


    while True:
        pass

   # print('Done Scraping Data -- find the csv file in the same directory :)')
    




# import csv
# import random
# import requests
# from bs4 import BeautifulSoup
# from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
# import requests
# import queue
# import threading
# lock = threading.Lock()

# q = queue.Queue()
# valid_proxies = []



# with open('proxyscrape_premium_http_proxies.txt', 'r') as f:
    
#      proxies = f.read().split('\n')
#      for proxy in proxies:
#          q.put(proxy)



# def check_proxy():
     
#      global q
#      while not q.empty():
          
#           cur_proxy = q.get()

#           #print(f'Checking proxy {cur_proxy}')

#           try:
#                 r = requests.get('https://httpbin.org/ip', proxies={'https': cur_proxy ,'http' : cur_proxy}, timeout=5)
#                 print(r.json())
#                 print(f'Proxy {cur_proxy} is valid')
#                 valid_proxies.append(cur_proxy)

#           except Exception as e:
#                 # print(f'Proxy {cur_proxy} is invalid')
#                 continue
          
#      return valid_proxies


# for i in range(10):
#      t = threading.Thread(target=check_proxy)
#      t.start()


# def scrape_data(url, name, rating, reviews, total_duration):
#     try:

#         cur_proxy = get_proxy() 
#         response = requests.get(url, proxies={'https': cur_proxy, 'http': cur_proxy}, timeout=15)
#         print(f'using proxy {cur_proxy}')
#         if response.status_code  == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')

#             ratings = soup.find_all('span', class_ = 'course-ratings-label')
#             print(ratings)
#             reviews = soup.find_all('span', class_ = 'course-rating-count')
#             durations = soup.find_all('div', class_ =  'course-info')
#             names = soup.find_all('h4', class_ = 'course-name')

#             with lock:

#                 for cur in ratings:
#                     rating.append(cur.text)

#                 for rev in reviews:
#                     reviews.append(rev.text)

#                 for dur in durations:
#                     total_duration.append(dur.text)

#                 for n in names:
#                     name.append(n.text)
#         else:

#             print(f"Error in scraping data: {response.status_code}")

#     except Exception as e:
#         print(f"Error in scraping data: {e}")



# def collect_valid_ips():
#     valid_ips = check_proxy()
#     return valid_ips


# def get_proxy():
#     valid_ips = collect_valid_ips()
#     if valid_ips:
#         return random.choice(valid_ips)
#     else:
#         print("No proxies available.")
#         return None


# def automate(base_url, suffix, name, rating, reviews, total_duration):
#     print('Scraping data from the website...')
#     total_pages = 9

#     for i in range(1, total_pages + 1):
#         url = base_url + str(i) + suffix
#         print(f'Getting data from {url}')
#         print('\n')
#         print('\n')
#         scrape_data(url, name, rating, reviews, total_duration)


# def make_csv(file_name, headers, *lists):
#     csv_filename = file_name + ".csv"
#     transposed_lists = list(zip(*lists))

#     with open(csv_filename, mode='w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(headers)
#         for row in transposed_lists:
#             writer.writerow(row)

#     print(f"CSV file '{csv_filename}' has been created.")


# if __name__ == "__main__":
#     base_url = 'https://www.mygreatlearning.com/data-science/free-courses?p='
#     suffix = '#subject-courses-section'
#     name = []
#     rating = []
#     reviews = []
#     total_duration = []

#     automate(base_url, suffix, name, rating, reviews, total_duration)
#     make_csv("output", ["Name", "Rating", "Reviews", "Total Duration"], name, rating, reviews, total_duration)



