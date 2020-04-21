"""A QuestionController Module."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller


class QuestionController(Controller):
    """QuestionController Controller Class."""

    def __init__(self, request: Request):
        self.request = request

    def index(self, view: View):
        return view.render('questions.index')
