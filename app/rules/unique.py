""" A unique validation """

from masonite.validation import BaseValidation
from app.User import User

class unique(BaseValidation):
    """A unique validation class
    """

    def passes(self, attribute, key, dictionary):
        """The passing criteria for this rule.

        This should return a True boolean value.

        Arguments:
            attribute {mixed} -- The value found within the dictionary
            key {string} -- The key in the dictionary being searched for.
                            This key may or may not exist in the dictionary.
            dictionary {dict} -- The dictionary being searched

        Returns:
            bool
        """
        return attribute not in User.all().pluck('email')

    def message(self, key):
        """A message to show when this rule fails

        Arguments:
            key {string} -- The key used to search the dictionary

        Returns:
            string
        """
        return 'The email has already been taken.'

    def negated_message(self, key):
        """A message to show when this rule is negated using a negation rule like 'isnt()'

        For example if you have a message that says 'this is required' you may have a negated statement
        that says 'this is not required'.

        Arguments:
            key {string} -- The key used to search the dictionary

        Returns:
            string
        """
        return '{} is not required'.format(key)