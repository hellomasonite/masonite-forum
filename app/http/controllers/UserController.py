from app.User import User


class UserController:
    ''' Controller For Welcoming The User '''

    def show(self, Request):
        try:
            user = User.find_or_fail(Request.param('id'))
        except:
            pass
        return view('users/show', {'user': user})
