from bs4 import  BeautifulSoup
from requests_html import HTMLSession

s = HTMLSession()

searchterm = 'sdcard'


#url for amazon website

url = f'https://www.amazon.co.uk/s?k={searchterm}&qid=1616907527&ref=sr_pg_1'

# To get the data from url
def getdata(url):
    r = s.get(url)
    r.html.render(sleep = 1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

#Scrape the data form website

def getdeals(soup):
    products = soup.find_all('div', {'data-component-type' :'s-search-result'})

    for item in products:

        #Extracting the title
        title = item.find('span', {'class' : "a-size-medium a-color-base a-text-normal"}).text.strip()

        #Extracting the links from amazon website
        links = item.find('a',  {'class' : 'a-link-normal a-text-normal'})['href']

        #Scraping the reviews products
        try:
            reviews = item.find('span', {'class' : 'a-size-base'}).text.strip()

        except:
            reviews = 0



#soup = getdata(url)
#print(getdeals(soup))

