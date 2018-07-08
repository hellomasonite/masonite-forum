from orator.migrations import Migration


class CreateVotesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('votes') as table:
            table.increments('id')
            table.integer('value').default(0)
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.integer('question_id').unsigned().nullable()
            table.foreign('question_id').references('id').on('questions')
            table.integer('answer_id').unsigned().nullable()
            table.foreign('answer_id').references('id').on('answers')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('votes')
