''' A Module Description '''
from masonite.facades.Auth import Auth
from app.Question import Question

class HomeController(object):
    ''' Home Dashboard Controller '''

    def __init__(self):
        pass
    
    def index(self):
        questions = Question.all()
        return view('index', {'questions': questions})
