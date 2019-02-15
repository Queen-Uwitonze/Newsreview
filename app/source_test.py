import unittest
from models import source
News = source.News

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News('Germ killing robot slips into your hotel bedsheets','nnc','description','https://edition.cnn.com/','Queen')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News))


if __name__ == '__main__':
    unittest.main()