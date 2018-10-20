''' A Question Database Model '''
from config.database import Model
from orator.orm import belongs_to, has_many
from app.Answer import Answer
from app.Vote import Vote
from markdown2 import Markdown

class Question(Model):
    __fillable__ = ['title', 'user_id', 'body', 'tags', 'category_id']
    __table__ = 'questions'

    @belongs_to('user_id', 'id')
    def user(self):
        from app.User import User
        return User
    
    @belongs_to('category_id', 'id')
    def category(self):
        from app.Category import Category
        return Category
    
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
    
    def body_converted(self):
        markdowner = Markdown()
        return markdowner.convert(self.body)
    
    def get_tags(self):
        return self.tags.split(',')
    
