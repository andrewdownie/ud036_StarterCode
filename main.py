from movie_metadata import movie_metadata
from fresh_tomatoes import *

# In main.py (this file):
#   First: a list is created to hold movie meta data, and then meta data for
#          movies are added to this list.
#   Finally: this list is passed to open_movies_page function in the
#            fresh_tomatoes module, the open_movie_page function  then creates
#            the html page.

movieList = []

movieList.append(
    movie_metadata(
        "Anchorman: The Legend of Ron Burgundy",
        "http://www.vhsisland.com/wp-content/uploads/2013/09/anchorman.jpg",
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
        "http://e.snmc.io/lk/f/l/98ef95be769a877de5a4cc6204a06866/5700650.jpg",
        "https://www.youtube.com/watch?v=hEJnMQG9ev8"
    )
)

open_movies_page(movieList)
