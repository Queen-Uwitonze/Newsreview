class Article:
    '''
    Article class to define Source Objects
    '''

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):
        self.id =id
        self.name=name
        self.author=author
        self.description = description
        self.url = url
        self.urlToImage=urlToImage
        self.publishedAt =publishedAt
        self.content = content 
        
        