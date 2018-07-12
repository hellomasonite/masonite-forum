''' A Question Database Model '''
from config.database import Model
from orator.orm import belongs_to, has_many
from app.Answer import Answer
from app.Vote import Vote

class Question(Model):
    __fillable__ = ['title', 'user_id', 'body', 'tags']
    __table__ = 'questions'

    @belongs_to('user_id', 'id')
    def user(self):
        from app.User import User
        return User
    
    @has_many
    def answers(self):
        return Answer
    
    def votes(self, id):
        # vote = Vote.where('question_id', id).last()
        # print(vote)
        votes = Vote.where('question_id', id).get()
        if votes.count() > 0:
            return votes.last().value
        
        return 0
    
    def get_tags(self):
        return self.tags.split(',')
    
