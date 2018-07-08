''' A Question Database Model '''
from config.database import Model
from orator.orm import belongs_to, has_many
from app.Answer import Answer

class Question(Model):
    __fillable__ = ['title', 'user_id', 'body']
    __table__ = 'questions'

    @belongs_to('user_id', 'id')
    def user(self):
        from app.User import User
        return User
    
    @has_many
    def answers(self):
        return Answer
    
