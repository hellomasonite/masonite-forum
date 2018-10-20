''' A Category Database Model '''
from config.database import Model
import random

class Category(Model):
    __fillable__ = ['name']

    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))