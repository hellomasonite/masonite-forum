"""A HomeController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite import Queue
from app.jobs.SendEmailConfirmation import SendEmailConfirmation

class HomeController(Controller):
    """HomeController Controller Class."""

    def __init__(self, request: Request):
        """HomeController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, queue: Queue):
        return view.render('home')
