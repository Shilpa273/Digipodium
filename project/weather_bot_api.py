import requests
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'lxml')
      

def get_weather():
    soup = get_soup('https://weather.com/en-IN/weather/today/l/a078a461b26f5aa0696d12e2ba79db07d0d67a205c3dc3917873f4118f558cec')     
    target = soup.find('div',attrs={'class':'CurrentConditions--columns--3KgfN'})
    weather = target.find('div',attrs={'class':'CurrentConditions--primary--2SVPh'})
    data=[]
    for item in weather:
        title = item.find()