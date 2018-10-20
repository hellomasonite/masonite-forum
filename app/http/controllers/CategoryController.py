''' A Module Description '''
from app.Category import Category
from app.Question import Question

class CategoryController:
    ''' Class Docstring Description '''

    def index(self, Request):
        page = Request.input('page', 1)
        category_id = Request.param('id')
        try:
            category = Category.find_or_fail(category_id)
        except:
            pass
        categories = Category.all()
        questions = Question.where('category_id', category.id).paginate(10, int(page))

        return view('index', {'questions': questions, 'categories': categories})
