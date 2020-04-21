from masonite.routes import Get, Post, RouteGroup


API_ROUTES = [
    RouteGroup([
        # Tags...
        Get('/tags', 'TagController@index').name('tags.index'),

    ], name='api.', namespace='api.', prefix='/api'),
]