"""The RegisterController Module."""
from masonite import Queue
from masonite.auth import Auth, MustVerifyEmail
from masonite.managers import MailManager
from masonite.request import Request
from masonite.view import View

from app.jobs.SendEmailConfirmation import SendEmailConfirmation
from app.rules.auth.RegisterRequest import RegisterRequest


class RegisterController:
    """The RegisterController class."""

    def __init__(self):
        """The RegisterController Constructor."""
        pass

    def show(self, view: View):
        return view.render('auth/register')

    def store(self, request: Request, mail_manager: MailManager, auth: Auth, queue: Queue):
        errors = request.validate(RegisterRequest)

        if errors:
            return request.back().with_errors(errors).with_input()

        user = auth.register({
            'name': request.input('name'),
            'password': request.input('password'),
            'email': request.input('email'),
        })

        if isinstance(user, MustVerifyEmail):
            queue.push(SendEmailConfirmation)
            #user.verify_email(mail_manager, request)

        # Login the user
        if auth.login(request.input('email'), request.input('password')):
            # Redirect to the homepage
            return request.redirect('/')

        # Login failed. Redirect to the register page.
        return request.back().with_input()