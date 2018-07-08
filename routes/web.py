''' Web Routes '''
from masonite.helpers.routes import get, post, group

ROUTES = [
    get('/', 'HomeController@index').name('welcome'),
    get('/login', 'LoginController@show'),
    get('/logout', 'LoginController@logout').middleware('auth'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show'),
    post('/register', 'RegisterController@store'),
    get('/ask', 'QuestionController@create').middleware('auth'),
    post('/questions', 'QuestionController@store').middleware('auth'),
    get('/questions/@id', 'QuestionController@show'),
    post('/questions/@id/answers', 'AnswerController@store').middleware('auth'),
    get('/questions/@id/upvote', 'QuestionController@upvote').middleware('auth'),
    get('/questions/@id/downvote', 'QuestionController@downvote').middleware('auth'),
    get('/me/questions', 'QuestionController@questions').middleware('auth'),
    get('/me/answers', 'AnswerController@answers').middleware('auth'),
]
