''' A Vote Database Model '''
from config.database import Model

class Vote(Model):
    __table__ = 'votes'

    __fillable__ = ['question_id', 'user_id', 'answer_id', 'value']
