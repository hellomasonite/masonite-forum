''' A Module Description '''
from masonite.facades.Auth import Auth


class LoginController(object):
    ''' Login Form Controller '''

    def __init__(self):
        pass

    def show(self, Request, Application):
        ''' Show the login page '''
        return view('auth/login', {'app': Application, 'Auth': Auth(Request)})

    def store(self, Request, Session):
        if Auth(Request).login(Request.input('email'), Request.input('password')):
            Session.flash('success', 'Logged successfuly!')
            return Request.redirect('/')
        else:
            Session.flash('danger', 'Incorrect username/password!')
            return Request.redirect('/login')

    def logout(self, Request, Session):
        Auth(Request).logout()
        Session.flash('success', 'You\'re logged out. Have a great day!')
        return Request.redirect('/login')
