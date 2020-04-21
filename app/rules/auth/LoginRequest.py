""" A LoginRequest validation enclosure """

from masonite.validation import RuleEnclosure, required, email


class LoginRequest(RuleEnclosure):
    """A LoginRequest validation enclosure class.
    """

    def rules(self):
        return [
            required(['email', 'password']),
            email('email')
        ]