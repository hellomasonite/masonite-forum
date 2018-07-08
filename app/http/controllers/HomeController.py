''' A Module Description '''
from masonite.facades.Auth import Auth

class HomeController(object):
    ''' Home Dashboard Controller '''

    def __init__(self):
        pass
    
    def index(self):
        return view('index')
