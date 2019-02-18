from flask import render_template
from app import app
from .request import get_news
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Queens News Review Website Online'
    general_news = get_news('business')

    return render_template('index.html', title = title, general = general_news)

