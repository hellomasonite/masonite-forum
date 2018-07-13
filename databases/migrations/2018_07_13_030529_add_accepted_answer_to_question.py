from orator.migrations import Migration


class AddAcceptedAnswerToQuestion(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('questions') as table:
            table.integer('accepted_answer').unsigned().nullable()
            table.foreign('accepted_answer').references('id').on('answers')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('questions') as table:
            pass
