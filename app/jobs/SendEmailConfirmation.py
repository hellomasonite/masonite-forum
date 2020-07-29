"""A SendEmailConfirmationJob Queue Job."""
import time
from masonite import Mail
from masonite.auth import Sign
from masonite.queues import Queueable
from masonite.request import Request


class SendEmailConfirmation(Queueable):
    """A SendEmailConfirmation Job."""

    def __init__(self, request: Request, mail: Mail):
        """A SendEmailConfirmation Constructor."""
        self.request = request
        self.mail = mail

    def handle(self):
        """Logic to handle the job."""
        print('job executed...')
        sign = Sign()

        token = sign.sign("{0}::{1}".format(self.id, time.time()))
        link = "{0}/email/verify/{1}".format(self.request.environ["HTTP_HOST"], token)

        self.mail.driver('smtp')\
            .to(self.request.user().email, {
                "name": self.request.user().name,
                "email": self.request.user().email,
                "link": link
            })\
            .template('mail/verifymail')\
            .send()
