from flask import render_template
from app import app
from .request import get_news
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/News/<news_source>')
def News(news_source):

    '''
    View NEWS page function that returns the news details page and its data
    '''

    update_news = get_news('update')
    print(Update-News)
    title = 'Queens News Review Website Online'
    return render_template('index.html', title = title,update = update_news)