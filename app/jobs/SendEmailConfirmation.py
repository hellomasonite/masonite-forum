"""A SendEmailConfirmation Queue Job."""
import time, os
from masonite import Mail
from masonite.auth import Sign
from masonite.queues import Queueable
from masonite.request import Request
from masonite import env


class SendEmailConfirmation(Queueable):
    """A SendEmailConfirmation Job."""

    def __init__(self, mail: Mail):
        """A SendEmailConfirmation Constructor."""
        self.mail = mail

    def handle(self, user):
        """Logic to handle the job."""
        token = Sign().sign("{0}::{1}".format(user.id, time.time()))
        link = "{0}/email/verify/{1}".format(env('APP_URL'), token)

        self.mail.driver('smtp').subject('Welcome To Masonite Forum')\
            .to(user.email)\
            .template('emails/email_confirmation.html', {
                "name": user.name,
                "email": user.email,
                "link": link
            })\
            .send()
