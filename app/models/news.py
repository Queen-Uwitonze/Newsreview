class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url,language,country,category):
        self.id =id
        self.name=name
        self.description = description
        self.url = url
        self.category=category
        self.language = language 
        self.country =country
        