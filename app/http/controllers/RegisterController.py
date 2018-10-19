''' A Module Description '''
from validator import Required, Not, Blank, validate, Length
from masonite.facades.Auth import Auth
from config import auth
import bcrypt


class RegisterController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request):
        ''' Show the registration page '''
        return view('auth/register')

    def store(self, Request, Session):
        ''' Register a new user '''
        ok, errors = self.validate_input(Request.all())

        if not ok:
            display = ''
            for error in errors:
                Session.flash(error, '{0} {1} \n\n\n'.format(error.title(), errors[error][0]))
            return Request.redirect('/register')

        # register the user
        password = bytes(bcrypt.hashpw(
            bytes(Request.input('password'), 'utf-8'), bcrypt.gensalt()
        )).decode('utf-8')

        auth.AUTH['model'].create(
            name=Request.input('name'),
            password=password,
            email=Request.input('email'),
        )

        # login the user
        # redirect to the homepage
        if Auth(Request).login(Request.input(auth.AUTH['model'].__auth__), Request.input('password')):
            Session.flash('success', 'Logged successfuly!')
            return Request.redirect('/')

    def validate_input(self, data):
        rules = {
            'name': [Required, Not(Blank()),Length(3)],
            'email': [Required, Not(Blank())],
            'password': [Required, Not(Blank()),Length(6)],
        }

        return validate(rules, data)