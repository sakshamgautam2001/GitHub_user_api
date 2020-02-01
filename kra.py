import mechanize
from bs4 import BeautifulSoup 
import ssl
import requests

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Firefox')]


def find_repo(user):

    # GITHUB WEBSITE DETAILS
    URL = "https://github.com/"+user


    r=requests.get(URL)

    soup=BeautifulSoup(r.content,'html5lib')

    # print(soup.prettify())

    quotes=[]   # A list to store quotes

    table=soup.find('div',attrs={'class','application-main'})

    # print(table.prettify())

    for row in table.findAll('span',attrs={'class','repo'}):
        quote=row.text
        quotes.append(quote)

    return(quotes)