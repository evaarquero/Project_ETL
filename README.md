# W5_project_ETL - Musical artist / Events / Spotify

Project repository for ETL(extract transfer load) project.

The aim of the project is to gather a big dataset, having:
- Three different sources.
- Using at least 2 of the methods from the course. 
- cleaning and exploring data, though functions, pandas, s
- building a dataset (SQL or Mongo)


My three sources with their method were:
- Charmaster web scrapping: from chartmasters website, to get the 1000 first [most streamed artists ever](https://chartmasters.org/most-streamed-artists-ever-on-spotify/)

- API get: using [spotipy ](https://spotipy.readthedocs.io/en/2.19.0/) library for accessing the Spotify API. 

- Web scrapping: songkick. getting the upcoming and past concerts from musical artists wanted. 

## Charmaster web scrapping
Through beautiful soup, i have scrapped the table in [charmasters](https://chartmasters.org/most-streamed-artists-ever-on-spotify/)

![charmasters](/mnt/c/Users/Palmira/Desktop/Ironhack/Semana4/project_ETL/images/charmasters.png)



## Cracking spotify with spotipy 
[Spotipy ](https://spotipy.readthedocs.io/en/2.19.0/) allows us to get into the spotify API through a friendly library. 
From each artist, spotify provides artist main information for doing searches in spotify, main albums, genres, popularity, followers. 

The first idea to get from spotify were the reproduction numbers from each of the artist, which it was not provided or allowed to get from Spotify. They have created a popularity rating, based on reproductions and time when they happened. 

![Spotipy](https://github.com/evaarquero/project_ETL/blob/main/images/popularity.PNG)

To see the proccess, the notebook is  `3-spotipy-loop.ipnyb`

## Songkick Web Scrapping 
[songkick ](https://www.songkick.com/) is a website where all recent past and future concerts from a musical artist are listed. The jupyter notebook of the process is  `4-scrapping-songkick.ipnyb`


![songkick](https://github.com/evaarquero/project_ETL/blob/main/images/songkick.PNG)


I created a loop in order to inspect the page and having the next 20 events and previous 20 events. The defined function can be imported for one or multiple artist in `songkick.py`


## mySQL queries
I created the database in SQL from the jupyter notebook `5-sql_queries.ipnyb`

![Power_BI](https://github.com/evaarquero/project_ETL/blob/main/images/mySQL.PNG)

## Data visualization
in order to visualized, power bi could be a great tool to represent the data for the concerts.

![Power_BI](https://github.com/evaarquero/project_ETL/blob/main/images/power_BI.PNG)

Extra work to be done for data visualization, in terms of streams values and ranking of the artists. The power BI file is saved as `artist_db.pbix`. 

