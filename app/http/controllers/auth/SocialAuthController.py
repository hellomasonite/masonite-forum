"""A SocialAuthController Module."""

from app.User import User
from masonite.view import View
from socialite import Socialite
from masonite.request import Request
from masonite.controllers import Controller


class SocialAuthController(Controller):
    """SocialAuthController Controller Class."""

    def login(self, request: Request, socialite: Socialite):
        """Redirect the user to GitHub"""
        return socialite.driver('github').redirect()

    def callback(self, request: Request, socialite: Socialite):
        user = socialite.driver('github').user()
        dd(user)
        # try:

        # except:
        #     return request.redirect('/login')

        return request.redirect('/')
