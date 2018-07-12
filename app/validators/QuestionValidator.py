from masonite.validator import Validator
from validator import Required, Not, Blank, validate, Length

class QuestionValidator(Validator):

    def validate_new_form(self):
        self.request.request_variables['tags'] = self.request.input('tags').split(',')
        return self.validate({
            'title': [Required, Not(Blank())],
            'body': [Required, Not(Blank())],
            'tags': [Required, Length(1, maximum=5)],
        })
