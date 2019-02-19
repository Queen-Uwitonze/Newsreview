class Article:
    '''
    Article class to define Source Objects
    '''

    def __init__(self,title,author,description,url,urlToImage,publishedAt,content):
        self.title=title
        self.author=author
        self.description = description
        self.url = url
        self.urlToImage=urlToImage
        self.publishedAt =publishedAt
        self.content = content 
        
        