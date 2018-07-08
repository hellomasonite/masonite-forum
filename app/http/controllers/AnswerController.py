''' A Module Description '''
from validator import Required, Not, Blank, validate
from app.Question import Question
from app.Answer import Answer

class AnswerController:
    ''' Class Docstring Description '''

    def store(self, Request, Session):
        ok, errors = self.validate_input(Request.all())
        id = Request.param('id')
        if not ok:
            display = ''
            for error in errors:
                display += '{0} {1} \n\n\n'.format(error.title(), errors[error][0])
            Session.flash('danger', display)
            return Request.redirect('/questions/@id', {'id': id})
        
        Answer.create(
            body=Request.input('body'),
            user_id=Request.user().id,
            question_id=id
        )
        Session.flash('success', 'Answer added successfuly!')
        return Request.redirect('/questions/@id', {'id': id})

    def validate_input(self, data):
        rules = {
            'body': [Required, Not(Blank())]
        }
        return validate(rules, data)