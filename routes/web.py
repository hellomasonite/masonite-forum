''' Web Routes '''
from masonite.helpers.routes import get, post, group
from masonite.routes import RouteGroup

ROUTES = [
    get('/', 'HomeController@index').name('welcome'),
    get('/login', 'LoginController@show').name('login'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show'),
    post('/register', 'RegisterController@store'),
    get('/questions/@id', 'QuestionController@show'),


    RouteGroup([
        get('/logout', 'LoginController@logout'),
        get('/ask', 'QuestionController@create').name('ask'),

        # Question Routes
        RouteGroup([
            post('', 'QuestionController@store').name('list'),
            post('/@id/answers', 'AnswerController@store').name('answers'),
            get('/@id/upvote', 'QuestionController@upvote').name('upvote'),
            get('/@id/downvote', 'QuestionController@downvote').name('downvote'),
        ], prefix='/questions', name='question.'),

        # Me Routes
        RouteGroup([
            get('/questions', 'QuestionController@questions').name('questions'),
            get('/answers', 'AnswerController@answers').name('answers'),
        ], prefix='/me', name='me.')
    ], middleware = ('auth',)),
]
