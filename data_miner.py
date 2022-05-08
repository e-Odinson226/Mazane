from webbrowser import get
import requests as req
from bs4 import BeautifulSoup

def get_html(url):
    re = req.request('GET', url)
    return re.text


def get_posts(raw_html):
    page_html = BeautifulSoup(raw_html, 'lxml')
    posts_holder_html = page_html.find('div',class_="flex-col card-holder")
    posts_html = posts_holder_html.find_all("div")
    return posts_html

#def get_post():
#    post_detail = {}
#    post_detail["icon-location"] = posts_html.f
#    post_detail["icon-residential"] = 
#    post_detail["icon-rooms"] = 
#    post_detail["icon-area"] = 
#---------------Driver---------------

# finding [  <div _ngcontent-kilid-portal-c153="" class="flex-col card-holder">  ]
try:
    raw_html = get_html('https://kilid.com/buy/tehran?listingTypeId=1&location=272905&page=2&sort=DATE_DESC')
    posts_list = get_posts(raw_html)
    print(posts_list[0].prettify())
except:
    raise Exception