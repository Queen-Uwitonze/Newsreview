import unittest
from models import news
Source = news.Source

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Source('abc-news','Australia most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.','https://abcnews.go.com','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Source))


if __name__ == '__main__':
    unittest.main()