"""Web Routes."""

from routes.api import API_ROUTES
from masonite.auth import Auth
from masonite.routes import Get, Post

ROUTES = [
    # Questions...
    Get('/', 'QuestionController@index').name('questions.index'),
]

ROUTES += API_ROUTES

# Authentication...
ROUTES += Auth.routes()
