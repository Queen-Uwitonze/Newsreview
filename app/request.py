from app import app
import urllib.request,json
from .models import news
# from .models import article

Source = news.Source
# Article = article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
base_url = app.config["ARTICLE_API_BASE_URL"]
def get_source(category):
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
            language = news_details_response.get('language')
            country = news_details_response.get('country')

            news_object = news(id,name,description,url,category,language,country)

    return news_object

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_sources = None

        if get_source_response['sources']:
            news_sources_list = get_source_response['sources']
            news_sources =  process_news(news_sources_list)


    return news_sources