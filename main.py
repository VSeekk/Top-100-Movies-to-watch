import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response= requests.get(URL)
movie_webpage= response.text
soup= BeautifulSoup(movie_webpage, "html.parser")

# movie_list= reversed(soup.find_all(name="h3", class_="title"))
movie_list= soup.find_all(name="h3", class_="title")[:: -1]
top_100 = []
for movie in movie_list:
    m= movie.getText()
    top_100.append(m)

# print(top_100)

with open("top100 movies.txt", "w") as file:
    file.write(str(top_100))









