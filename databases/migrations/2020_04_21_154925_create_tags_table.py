from orator.migrations import Migration


class CreateTagsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tags') as table:
            table.string('name').unique()
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tags')
