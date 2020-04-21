"""Web Routes."""

from masonite.auth import Auth
from routes.api import API_ROUTES
from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    # Questions...
    Get('/', 'QuestionController@index').name('questions.index'),

    # Social Authentication
    RouteGroup([
        # GitHub...
        Get('github', 'auth.SocialAuthController@login').name('login'),
        Get('github/callback', 'auth.SocialAuthController@callback').name('callback'),
    ], name='social.auth.', namespace='auth.', prefix='/auth'),

]

ROUTES += API_ROUTES

# Authentication...
ROUTES += Auth.routes()
