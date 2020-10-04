"""A LoginController Module."""

from masonite.auth import Auth
from masonite.view import View
from masonite.request import Request
from masonite.validation import Validator
from app.rules.auth.LoginRequest import LoginRequest


class LoginController:
    """Login Form Controller."""

    def __init__(self):
        """LoginController Constructor."""
        pass

    def show(self, request: Request, view: View):
        if request.user():
            return request.redirect('/')

        return view.render('auth/login')

    def store(self, request: Request, auth: Auth, validate: Validator):
        errors = request.validate(LoginRequest)

        if errors:
            return request.back().with_errors(errors).with_input()

        if auth.login(request.email, request.password):
            return request.redirect('/')

        return request.back().with_errors({
            'email': ['These credentials do not match our records.']
        })

    def logout(self, request: Request, auth: Auth):
        """Log out the user.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
            auth {masonite.auth.auth} -- The Masonite auth class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """
        auth.logout()
        return request.redirect('/')
