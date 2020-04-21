"""Tag Model."""

from config.database import Model


class Tag(Model):
    """Tag Model."""

    __fillable__ = ['name']