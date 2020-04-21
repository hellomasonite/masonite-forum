"""A TagController Module."""

import json
from app.Tag import Tag
from masonite.response import Response
from masonite.controllers import Controller


class TagController(Controller):
    """TagController Controller Class."""

    def index(self, response: Response):
        tags = Tag.all()

        return json.loads(tags.to_json())