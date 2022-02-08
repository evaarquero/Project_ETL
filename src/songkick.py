import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import regex as re


url_songkick = 'https://www.songkick.com/search?page=1&per_page=10&type=upcoming&query='
url_songkick2 = 'https://www.songkick.com/search?page=2&per_page=10&type=upcoming&query='

def Songkick_list(artists_name):
    concerts = []
    for i in artists_name:
        html = req.get(url_songkick+i).content
        soup = bs(html, 'html.parser')
        for e in soup.find_all("li" ,{"class":"concert event"}):
            # bucle para los conciertos
            location = e.find("p", {"class":"location"}).text.strip() # location
            date = e.find("p", {"class":"date"}).text.strip() # date
            concerts.append({
                'artist': i,
                'date': date,
                'location': location            
                })
        html2 = req.get(url_songkick2+i).content
        soup2 = bs(html2, 'html.parser')
        for e in soup2.find_all("li" ,{"class":"concert event"}):
            # bucle para los conciertos
            location = e.find("p", {"class":"location"}).text.strip() # location
            date = e.find("p", {"class":"date"}).text.strip() # date
            concerts.append({
                'artist': i,
                'date': date,
                'location': location          
               })
    artist_concerts = pd.DataFrame(concerts)
    return  artist_concerts


def Songkick_one(artist_name):
    concerts = []
    html = req.get(url_songkick+artist_name).content
    soup = bs(html, 'html.parser')
    for e in soup.find_all("li" ,{"class":"concert event"}):
        # bucle para los conciertos
        location = e.find("p", {"class":"location"}).text.strip() # location
        date = e.find("p", {"class":"date"}).text.strip() # date
        concerts.append({
            'artist': artist_name,
            'date': date,
            'location': location            
                })
    html2 = req.get(url_songkick2+artist_name).content
    soup2 = bs(html2, 'html.parser')
    for e in soup2.find_all("li" ,{"class":"concert event"}):
        # bucle para los conciertos
        location = e.find("p", {"class":"location"}).text.strip() # location
        date = e.find("p", {"class":"date"}).text.strip() # date
        concerts.append({
                'artist': artist_name,
                'date': date,
                'location': location          
               })
    artist_concerts = pd.DataFrame(concerts)
    return artist_concerts 