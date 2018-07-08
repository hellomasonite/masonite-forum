''' A Answer Database Model '''
from config.database import Model
from orator.orm import belongs_to

class Answer(Model):
    __table__ = 'answers'

    __fillable__ = ['question_id', 'user_id', 'body']

    @belongs_to('user_id', 'id')
    def user(self):
        from app.User import User
        return User