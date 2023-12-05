# Multipage scraping from data science -  greatlearning.com

import csv
import queue
import random
import threading
import pandas as pd
import requests
from bs4 import BeautifulSoup
import queue
import random
import threading
import requests
q = queue.Queue()
valid_proxies = []






def scrape_data(url, all_names, all_ratings, all_reviews):
    try:

        random_proxy = get_proxy()

        response = requests.get(url,proxies={'https':random_proxy ,'http' : random_proxy}, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        ratings = soup.find_all('span', class_='course-ratings-label')
        reviews = soup.find_all('span', class_='rating-count-label')
        names = soup.find_all('h2', class_='course-name')

        for cur in ratings:
            all_ratings.append(cur.text)

        for rev in reviews:
            all_reviews.append(rev.text)

        
        for n in names:
            all_names.append(n.text.strip())

    except Exception as e:
        print(f"Error in scraping data: {e}")





## This method is used to automate the process of and I scraped all 11 pages here
def automate(base_url, suffix, all_names, all_ratings, all_reviews):
    print('Scraping data from the website...Hold on It takes a while')
    print('\n')
    print('From the list of free proxy list - making a list of valid proxies')
    print('\n')
    print('Finding Valid proxies...')
    print('\n')
    total_pages = 11

    for i in range(1, total_pages + 1):
        url = base_url + str(i) + suffix
        print(f'Getting data from {url}')
        scrape_data(url, all_names, all_ratings, all_reviews)

        


# Generating csv file for final data
def make_csv(all_names, all_ratings, all_reviews):
    df = pd.DataFrame(list(zip(all_names, all_ratings, all_reviews)),
                      columns=["Name", "Rating", "Reviews"])
    
    print(df.head(10))
    df.to_csv('all_data.csv', index=False)




# free - trail 100 proxies list from proxyscrape.com
with open('proxyscrape_premium_http_proxies.txt', 'r') as f:
    
     proxies = f.read().split('\n')
     for proxy in proxies:
         q.put(proxy)



def check_proxy():
     
     while not q.empty():
          
          cur_proxy = q.get()

          #print(f'Checking proxy {cur_proxy}')

          try:
                r = requests.get('https://httpbin.org/ip', proxies={'https': cur_proxy ,'http' : cur_proxy}, timeout=5)
                print(r.json())
                print(f'Proxy {cur_proxy} is valid')
                valid_proxies.append(cur_proxy)

          except Exception as e:
                
                # print(f'Proxy {cur_proxy} is invalid')
                continue
          
     return valid_proxies


for i in range(10):
     t = threading.Thread(target=check_proxy)
     t.start()


def collect_valid_ips():
    valid_ips = check_proxy()
    return valid_ips


def get_proxy():
    all_valid_ips = collect_valid_ips()
    if all_valid_ips:
        return random.choice(all_valid_ips)
    else:
        #print("No proxies available.")
        return None




# main func
if __name__ == "__main__":
    
    all_names = []
    all_ratings = []
    all_reviews = []

    base_url = 'https://www.mygreatlearning.com/data-science/free-courses?p='
    suffix = '#subject-courses-section'

    automate(base_url, suffix, all_names, all_ratings, all_reviews)
    make_csv(all_names, all_ratings, all_reviews)


