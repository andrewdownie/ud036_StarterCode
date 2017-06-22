from movie_metadata import movie_metadata
from fresh_tomatoes import *

#In main.py (this file) a list is created to hold movie meta data, and then meta data for three movies are added to this list. 
#Finally this list is passed to open_movies_page function in the fresh_tomatoes module to add this media data to an html page dynamically.

movieList = []

movieList.append( 
    movie_metadata(
        "Anchorman: The Legend of Ron Burgundy", 
        "https://images-na.ssl-images-amazon.com/images/I/51DQR900C0L._SY445_.jpg", 
        "https://www.youtube.com/watch?v=-T3wnP91OnI"
    )
)

movieList.append( 
    movie_metadata(
        "Layer Cake", 
        "https://upload.wikimedia.org/wikipedia/en/e/e8/Layer_Cake_Poster.JPG", 
        "https://www.youtube.com/watch?v=e5R4iepdXqo"
    )
)

movieList.append( 
    movie_metadata(
        "Mad Max: Fury Road", 
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_UY1200_CR97,0,630,1200_AL_.jpg", 
        "https://www.youtube.com/watch?v=hEJnMQG9ev8"
    )
)

open_movies_page(movieList)
