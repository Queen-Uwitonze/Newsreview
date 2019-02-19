from app import app
import urllib.request,json
from .models import news,articles
Article =  articles.Article
# from .models import article

Source = news.Source
# Article = article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLE_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources =  process_news(news_sources_list)


    return news_sources

  

def process_news(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_sources: A list of news objects
    '''
    news_sources = []

    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description= news_item.get('description')
        url = news_item.get("url")
        category = news_item.get("category")
        language = news_item.get("language")
        country = news_item.get("country")
        

        if id:
            news_object = Source(id,name,description,url,category,language,country)
            news_sources.append(news_object)
         

    return news_sources

def get_news_sources(id):
    get_news_sources_details_url = base_url.format(id,api_key)
 

    with urllib.request.urlopen(get_news_sources_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
       
        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('original_name')
            description = news_details_response.get('description')
            url= news_details_response.get('url_path')
            category=news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')

            news_object = Source(id,name,description,url,category,language,country)
            

    return news_object


# this the part where we have displayed data or the second class Article

def get_news_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_articles_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_news_articles_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_articles = None

        if get_source_response['articles']:
            news_articles_list = get_source_response['articles']
            news_articles =  process_news_articles(news_articles_list)


    return news_articles

def process_news_articles(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_sources: A list of news objects
    '''
    news_articles = []

    for news_item in news_list:
        # id = news_item.get('id')
        author = news_item.get('author')
        title = news_item.get('title')
        description= news_item.get('description')
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        content = news_item.get("content")
       
        

        if urlToImage:
            news_object =Article(author,title,description,url,urlToImage,publishedAt,content)
            news_articles.append(news_object)
         

    return news_articles

