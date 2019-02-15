from flask import render_template
from app import app

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
    title = 'Queens News Review Website Online'
    return render_template('index.html', title = title)