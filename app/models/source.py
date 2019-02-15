class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,source,title,overview,poster):
        self.source =source
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        