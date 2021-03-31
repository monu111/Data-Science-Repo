from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

s = HTMLSession()

searchterm = 'dslr+camera'

# url for amazon website
#url = 'https://www.amazon.co.uk/s?k={searchterm}&qid=1616907527&ref=sr_pg_1'
url = f'https://www.amazon.co.uk/s?k={searchterm}&i=black-friday'


# 
def getdata(url):
    r = s.get(url)
    r.html.render(sleep = 1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

#
dealslist = []
def getdeals(soup):
    products = soup.find_all('div', {'data-component-type' : 's-search-result'})
    for item in products:

        # Scraping product name
        title = item.find('a', {'class': 'a-link-normal a-text-normal'}).text.strip()

        short_title = item.find('a', {'class': 'a-link-normal a-text-normal'}).text.strip()[:25]

        # Scraping the links of product
        link = item.find('a', {'class': 'a-link-normal a-text-normal'})['href']


        # Scraping the reviews of products
        try:
            reviews = item.find('span',{'class' : 'a-size-base'}).text.strip()
        except:
            reviews =  0


        # putting all item into list of dictionary
        saleitem = {
            'title' : title,
            'short_title' : short_title,
            'link' : link,
            'reviews' : reviews
             }
        dealslist.append(saleitem)
    return 

# Getting pages from amazon
def getnextpage(soup):
    page = soup.find('ul', {'class' : 'a-pagination'})
    if not page.find('li', {'class' : 'a-disabled a-last'}):  # if  not last page 
        
        url = 'https://www.amazon.co.uk' + str(page.find('li', {'class' : 'a-last'}).find('a')['href'])
        
        return url   # it will return  url through diff. pages
    else:
        return       # it will return nothing
        

# traversing through pages url 
while True:
    data = getdata(url)
    getdeals(data)
    url = getnextpage(data)  # extract url for every page on amazon website
    if not url:
        break
    else:
        
        print(url)
        print(len(dealslist))


# Creating the data frame
df = pd.DataFrame(dealslist)
df.to_csv('camera+dslr_amazon.csv', index = False)