from orator.migrations import Migration
from app.Category import Category

class SeedCategories(Migration):

    def __init__(self):
        self.categories = ['Databases', 'General', 'JavaScript', 'Masonite', 'Python', 'Servers', 'Orator', 'Craft', 'Testing', 'Tips']
        super().__init__()

    def up(self):
        for category in self.categories:
            Category.create(name=category)

    def down(self):
        for category in self.categories:
            Category.where('name', category).delete()