from orator.migrations import Migration


class CreateAnswersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('answers') as table:
            table.increments('id')
            table.text('body')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.integer('question_id').unsigned()
            table.foreign('question_id').references('id').on('questions')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('answers')
