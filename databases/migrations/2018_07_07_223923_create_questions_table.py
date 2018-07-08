from orator.migrations import Migration


class CreateQuestionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('questions') as table:
            table.increments('id')
            table.string('title')
            table.text('body')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('questions')
