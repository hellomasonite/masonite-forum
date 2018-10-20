''' User Model '''
from config.database import Model
from app.Question import Question
from app.Answer import Answer

class User(Model):
    ''' User Model '''

    __fillable__ = ['name', 'email', 'password']

    __auth__ = 'email'

    def questions(self):
        return Question.where('user_id', self.id).get()
    
    def answers(self):
        return Answer.where('user_id', self.id).get()
