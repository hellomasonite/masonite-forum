"""A SendWelcomeEmailJob Queue Job."""

from masonite.queues import Queueable
from masonite import Mail


class SendWelcomeEmailJob(Queueable):
    """A SendWelcomeEmailJob Job."""

    def __init__(self, mail: Mail):
        """A SendWelcomeEmailJob Constructor."""
        self.mail = mail

    def handle(self):
        """Logic to handle the job."""
        self.mail.driver('smtp').to('nioperas06@gmail.com').send('Welcome!')
