from orator.migrations import Migration


class AddTagsToQuestionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('questions') as table:
            table.string('tags')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('questions') as table:
            table.drop_column('tags')
