"""Masonite Socialite Config file"""

from masonite import env

""" The default strategy you need to use. You can write your own strategy """

# SOCIAL_AUTH_STRATEGY = "socialite.strategy.MasoniteStrategy"

"""
 The list of the providers you need to support in your project. 
 More information about the available backends at 
 https://python-social-auth.readthedocs.io/en/latest/backends/index.html
"""

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.linkedin.LinkedinOAuth2',
)

"""
 FACEBOOK Configurations
"""

SOCIAL_AUTH_FACEBOOK_KEY = env("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = env("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_REDIRECT_URI = env("SOCIAL_AUTH_FACEBOOK_REDIRECT_URI")
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email',
}

"""
 GOOGLE OAuth2 Configurations
"""

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = env("SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI")

"""
 GITHUB Configurations
"""

SOCIAL_AUTH_GITHUB_KEY = env("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = env("SOCIAL_AUTH_GITHUB_SECRET")
SOCIAL_AUTH_GITHUB_REDIRECT_URI = env("SOCIAL_AUTH_GITHUB_REDIRECT_URI")

"""
 LINKEDIN OAuth2 Configurations
"""

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = env("SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY")
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = env("SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET")
SOCIAL_AUTH_TWITTER_OAUTH2_REDIRECT_URI = env("SOCIAL_AUTH_TWITTER_OAUTH2_REDIRECT_URI")

"""
 TWITTER Configurations
"""

SOCIAL_AUTH_TWITTER_KEY = env("SOCIAL_AUTH_TWITTER_KEY")
SOCIAL_AUTH_TWITTER_SECRET = env("SOCIAL_AUTH_TWITTER_SECRET")
SOCIAL_AUTH_TWITTER_REDIRECT_URI = env("SOCIAL_AUTH_TWITTER_REDIRECT_URI")
