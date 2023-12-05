import csv
import random
import requests
from bs4 import BeautifulSoup
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
import requests
import queue
import threading

q = queue.Queue()
valid_proxies = []



with open('proxies.txt', 'r') as f:
    
     proxies = f.read().split('\n')
     for proxy in proxies:
         q.put(proxy)



def check_proxy():
     
     global q
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



def scrape_data(url, name, rating, reviews, total_duration):
    try:

        cur_proxy = get_proxy() 
        response = requests.get(url, proxies={'https': cur_proxy, 'http': cur_proxy}, timeout=15)
        print(f'using proxy {cur_proxy}')
        if response.status_code  == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            ratings = soup.find_all('span', class_ = 'course-ratings-label')
            print(ratings)
            reviews = soup.find_all('span', class_ = 'course-rating-count')
            durations = soup.find_all('div', class_ =  'course-info')
            names = soup.find_all('h4', class_ = 'course-name')

            for cur in ratings:
                rating.append(cur.text)

            for rev in reviews:
                reviews.append(rev.text)

            for dur in durations:
                total_duration.append(dur.text)

            for n in names:
                name.append(n.text)
        else:

            print(f"Error in scraping data: {response.status_code}")

    except Exception as e:
        print(f"Error in scraping data: {e}")



def collect_valid_ips():
    valid_ips = check_proxy()
    return valid_ips


def get_proxy():
    valid_ips = collect_valid_ips()
    if valid_ips:
        return random.choice(valid_ips)
    else:
        print("No proxies available.")
        return None


def automate(base_url, suffix, name, rating, reviews, total_duration):
    print('Scraping data from the website...')
    total_pages = 9

    for i in range(1, total_pages + 1):
        url = base_url + str(i) + suffix
        print(f'Getting data from {url}')
        scrape_data(url, name, rating, reviews, total_duration)


def make_csv(file_name, headers, *lists):
    csv_filename = file_name + ".csv"
    transposed_lists = list(zip(*lists))

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for row in transposed_lists:
            writer.writerow(row)

    print(f"CSV file '{csv_filename}' has been created.")


if __name__ == "__main__":
    base_url = 'https://www.mygreatlearning.com/data-science/free-courses?p='
    suffix = '#subject-courses-section'
    name = []
    rating = []
    reviews = []
    total_duration = []

    automate(base_url, suffix, name, rating, reviews, total_duration)
    make_csv("output", ["Name", "Rating", "Reviews", "Total Duration"], name, rating, reviews, total_duration)



