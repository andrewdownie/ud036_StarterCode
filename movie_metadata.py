# This class holds the 3 required pieces of meta data for a movie:
#   - the title of the movie
#   - url of the movies poster image
#   - the url of a trailer for the movie on youtube


class movie_metadata(object):
    title = '<BLANK>'
    poster_image_url = '<BLANK>'
    trailer_youtube_url = '<BLANK>'

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def PrintAll(self):
        # Prints all of the variables of this class to the command line.
        print("Movie info:")
        print("\t" + self.title)
        print("\t" + self.poster_image_url)
        print("\t" + self.trailer_youtube_url)
