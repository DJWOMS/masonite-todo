""" Category Model """

from masoniteorm.models import Model


class Category(Model):
    """Category Model"""
    __fillable__ = ["name"]
