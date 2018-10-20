from orator.migrations import Migration


class AddCategoriesToQuestionsTable(Migration):

    def up(self):
        with self.schema.table('questions') as table:
            table.integer('category_id').unsigned().nullable()
            table.foreign('category_id').references('id').on('categories')

    def down(self):
        with self.schema.table('questions') as table:
            table.drop_column('category_id')
