''' Web Routes '''
from masonite.helpers.routes import get, post, group

ROUTES = [
    get('/', 'HomeController@index').name('welcome'),
    get('/login', 'LoginController@show').name('login'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show'),
    post('/register', 'RegisterController@store'),
    get('/questions/@id', 'QuestionController@show'),

    # auth middleware
    get('/logout', 'LoginController@logout').middleware('auth'),
    get('/ask', 'QuestionController@create').middleware('auth'),
    group('/questions', [
        post('', 'QuestionController@store').middleware('auth'),
        post('/@id/answers', 'AnswerController@store').middleware('auth'),
        get('/@id/upvote', 'QuestionController@upvote').middleware('auth'),
        get('/@id/downvote', 'QuestionController@downvote').middleware('auth'),
    ]),
    get('/me/questions', 'QuestionController@questions').middleware('auth'),
    get('/me/answers', 'AnswerController@answers').middleware('auth'),
]
