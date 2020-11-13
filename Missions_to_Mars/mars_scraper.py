# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from splinter import Browser
from bs4 import BeautifulSoup
import time 
import pandas as pd


# %%
def init_browser():
    executable_path = {"executable_path": "C:/Users/Administrator/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# %% [markdown]
# # Scraping News from NASA

# %%
def nasa_news():
    browser = init_browser()
    articles = []
    paragraphs = []
    
    url = "https://mars.nasa.gov/news/"
    
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    news_title = soup.find_all('div', class_="content_title")
    news_p = soup.find_all('div', class_='article_teaser_body')
    
    for item in news_title:
        articles.append(item.get_text())
        
    for paragraphs in news_p:
        paragraphs.append(item.get_text())
    
    return [*zip(articles, paragraphs)]
    return html(table)
        
    
# nasa_news()


# %%
# return the first paragraph
# print(x[0][1])

# %% [markdown]
# # Featured Image from NASA JPL Mars Space Image

# %%
def mars_image():
    url = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser = init_browser()
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    img_source = soup.find(class_="carousel_item")['style']
    img_string = img_source.split("'")[1]
    base_url = 'https://jpl.nasa.gov'
    final_image_url = base_url + img_string
    return final_image_url


# %% [markdown]
# # Scraping table from Mars Facts using Pandas

# %%
def mars_facts():
    url = 'https://space-facts.com/mars/'
    facts_table = pd.read_html(url)
    mars_table = facts_table[0].to_json(orient='records')
    return 
# mars_facts()

# %% [markdown]
# # Getting high-res pictures of Mars Hemispheres

# %%
def mars_hemi():
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = init_browser()
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    title = []
    i = 0
    while i < 4:
        hemisphere = soup.find_all('h3')[i].text.strip()
        title.append(hemisphere)
        i += 1
    
    paths = []
    i = 0 
    while i < 8:
        path = soup.find_all('a', class_='itemLink product-item')[i]['href']
        paths.append(path)
        i += 2
    
    base_url = "https://astrogeology.usgs.gov"
    url_list = []
    
    for path in paths:
        url = base_url + path
        url_list.append(url)
    time.sleep(5)
        
    image_url = []
    for url in url_list:
        img_source = soup.find('img', class_="thumb")['src']
        img_url = base_url + img_source
        image_url.append(img_url)
#     print(image_url)
#
    hemi_image_urls = []
    i = 0
    while i < 4:
        hemi_image_urls.append({'title': title[i], 'image_url': image_url[i]})
        i += 1
    return hemi_image_urls
# mars_hemi()


# %%
#dictionary to return data

mars_data = {
    "Mars_News": nasa_news,
    "Mars_Image": mars_image,
    "Mars_Facts": mars_facts,
    "Mars_Hemis": mars_hemi
}

return nasa_news




