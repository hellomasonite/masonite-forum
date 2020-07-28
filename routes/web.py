"""Web Routes."""

from masonite.auth import Auth
from routes.api import API_ROUTES
from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    # Home...
    Get('/', 'HomeController@show').name('home'),

    # Questions...
    Get('/questions', 'QuestionController@index').name('questions.index'),

    # Social Authentication
    RouteGroup([
        # GitHub...
        Get('github', 'SocialAuthController@login').name('login'),
        Get('github/callback', 'SocialAuthController@callback').name('callback'),
    ], name='social.auth.', namespace='auth.', prefix='/auth'),

]

ROUTES += API_ROUTES

# Authentication...
ROUTES += Auth.routes()
