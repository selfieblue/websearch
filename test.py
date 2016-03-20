import requests
from bs4 import BeautifulSoup

def feed_data():
    url = "https://selfieblue.wordpress.com"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for link in soup.findAll('a',{'class':'feed-item'}):
        href = link.get('href')
        title = "Selfieblue's Blog"
        #title = link.string
        print("Title : "+ str(title) + " Link : "+ str(href))
        feed_images(href)
    
def feed_images(page_url):
    source_code = requests.get(page_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for img_name in soup.findAll('img',{'title':'image'}):
        image = img_name.get('src')
        print(image)
        
feed_data()
