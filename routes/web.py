"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'QuestionController@index').name('questions.index'),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
