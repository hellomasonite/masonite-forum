"""A SendResetEmailLinkJob Queue Job."""

from masonite.queues import Queueable


class SendResetEmailLinkJob(Queueable):
    """A SendResetEmailLinkJob Job."""

    def __init__(self):
        """A SendResetEmailLinkJob Constructor."""
        pass

    def handle(self):
        """Logic to handle the job."""
        pass
