""" A RegisterRequest validation enclosure """

from masonite.validation import RuleEnclosure
from masonite.validation import required, email, numeric, length


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
            # TODO
            length('password', min=6)
        ]