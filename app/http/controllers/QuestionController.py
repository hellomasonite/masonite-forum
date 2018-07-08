''' A Module Description '''
from validator import Required, Not, Blank, validate, Length
from app.User import User
from app.Question import Question

class QuestionController:
    ''' Class Docstring Description '''

    def show(self):
        pass

    def index(self):
        pass

    def create(self):
        return view('questions/new')

    def store(self, Request, Session):
        ok, errors = self.validate_input(Request.all())

        if not ok:
            display = ''
            for error in errors:
                display += '{0} {1} \n\n\n'.format(error.title(), errors[error][0])
            Session.flash('danger', display)
            return Request.redirect('/ask')
        
        Question.create(
            title=Request.input('title'),
            body=Request.input('body'),
            user_id=Request.user().id
        )
        Session.flash('success', 'Question added successfuly!')
        return Request.redirect('/')

    def edit(self):
        pass

    def update(self):
        pass

    def destroy(self):
        pass

    def validate_input(self, data):
        rules = {
            'title': [Required, Not(Blank())],
            'body': [Required, Not(Blank())]
        }

        return validate(rules, data)