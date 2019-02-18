from app import app
import urllib.request,json
from .models import news

Source = news.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

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
        description= news_item.get('description')
        url = news_item.get("url")
        category = news_item.get("category")
        language = news_item.get("language")
        country = news_item.get("country")
        

        if id:
            news_object = Source(id,description,url,category,language,country)
            news_sources.append(news_object)

    return news_sources