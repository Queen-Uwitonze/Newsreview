from flask import render_template
from app import app
from .request import get_news,get_news_sources
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Queens News Review Website Online'
    general_news = get_news('business')
    sport_news = get_news('sport')
    finances_news = get_news ('finance')
    return render_template('index.html', title = title, general = general_news,sport = sport_news,finance =finances_news )

@app.route('/news_sources/<id>')
def news_sources(id):

    '''
    View news_sources page function that returns the news details page and its data
    '''
    news = get_news_sources(id)
    title = f'{news.title}'

    return render_template('movie.html',title = title,news = news)