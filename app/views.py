from flask import render_template
from app import app
from .request import get_news,get_news_articles
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Queens News Review Website Online'
    general_news = get_news('business')
    entertainment_news = get_news('entertainment')
   
 
    return render_template('index.html', title = title, general = general_news,entertainment = entertainment_news )

@app.route('/news_sources/<id>')
def source(id):

    '''
    View news_sources page function that returns the news details page and its data
    '''
    news = get_news_articles(id)
    title = f'{id}'
   

    return render_template('news.html',title = title,news = news)

