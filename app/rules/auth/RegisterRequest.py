""" A RegisterRequest validation enclosure """

from app.User import User
from app.rules.unique import unique
from masonite.validation import RuleEnclosure
from masonite.validation import required, email, numeric, length, isnt, is_in


class RegisterRequest(RuleEnclosure):
    """A RegisterRequest validation enclosure class.
    """

    def rules(self):
        """Used to return a list of rules in order to make some validation
        more reusable.

        Returns:
            list -- List of rules
        """
        return [
            required(['name', 'email', 'password']),
            email('email'),
            unique('email'),
            length('password', min=6)
        ]