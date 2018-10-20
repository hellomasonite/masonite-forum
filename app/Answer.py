''' A Answer Database Model '''
from config.database import Model
from orator.orm import belongs_to
from markdown2 import Markdown

class Answer(Model):
    __table__ = 'answers'

    __fillable__ = ['question_id', 'user_id', 'body']

    @belongs_to('user_id', 'id')
    def user(self):
        from app.User import User
        return User
    
    @belongs_to('question_id', 'id')
    def question(self):
        from app.Question import Question
        return Question
    
    def body_converted(self):
        markdowner = Markdown()
        return markdowner.convert(self.body)