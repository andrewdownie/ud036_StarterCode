class MovieMetadata(object):
    movieTitle = '<Default movie title>'
    boxArtUrl = '<Default box art url>'
    trailerUrl = '<Default trailer url>'


    def __init__(self, movieTitle, boxArtUrl, trailerUrl):
        self.movieTitle = movieTitle
        self.boxArtUrl = boxArtUrl
        self.trailerUrl = trailerUrl
    
    def PrintContents(self):
        print("Movie info:")
        print("\t" + self.movieTitle)
        print("\t" + self.boxArtUrl)
        print("\t" + self.trailerUrl)