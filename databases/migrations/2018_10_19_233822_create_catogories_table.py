from orator.migrations import Migration


class CreateCatogoriesTable(Migration):

    def up(self):
        with self.schema.create('categories') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()

    def down(self):
        self.schema.drop('categories')
