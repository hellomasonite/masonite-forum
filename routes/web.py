''' Web Routes '''
from masonite.helpers.routes import get, post
from masonite.routes import RouteGroup as group

ROUTES = [
    get('/', 'HomeController@index').name('welcome'),
    get('/login', 'LoginController@show').name('login'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show'),
    post('/register', 'RegisterController@store'),
    get('/questions/@id', 'QuestionController@show').name('question'),


    group([
        get('/logout', 'LoginController@logout'),
        get('/ask', 'QuestionController@create').name('ask'),

        # Question Routes
        group([
            post('', 'QuestionController@store').name('list'),
            post('/@id/answers', 'AnswerController@store').name('answers'),
            post('/@id/answers/@answer_id/accept', 'QuestionController@accept_answer').name('accept'),
            get('/@id/upvote', 'QuestionController@upvote').name('upvote'),
            get('/@id/downvote', 'QuestionController@downvote').name('downvote'),
        ], prefix='/questions', name='question.'),

        # Me Routes
        group([
            get('/questions', 'QuestionController@questions').name('questions'),
            get('/answers', 'AnswerController@answers').name('answers'),
        ], prefix='/me', name='me.')
    ], middleware = ('auth',)),
]
