''' A Module Description '''
from validator import Required, Not, Blank, validate
from app.Question import Question
from app.Answer import Answer

class AnswerController:
    ''' Class Docstring Description '''

    def store(self, Request, Session):
        print('hehe')
        ok, errors = self.validate_input(Request.all())
        id = Request.param('id')
        if not ok:
            display = ''
            for error in errors:
                Session.flash(error, '{0} {1} \n\n\n'.format(error.title(), errors[error][0]))
            return Request.redirect_to('questions.show', {'id': id})
        
        Answer.create(
            body=Request.input('body'),
            user_id=Request.user().id,
            question_id=id
        )
        return Request.redirect('/questions/@id', {'id': id})
    
    def answers(self, Request):
        answers = Answer.where('user_id', Request.user().id).get()
        return view('answers/me', {'answers': answers})

    def validate_input(self, data):
        rules = {
            'body': [Required, Not(Blank())]
        }
        return validate(rules, data)