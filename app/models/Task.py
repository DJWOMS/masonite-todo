""" Task Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Task(Model):
    """Task Model"""
    __fillable__ = ["text", "done", "end_date", "category_id"]

    @belongs_to('category_id', 'id')
    def category(self):
        from app.models.Category import Category
        return Category
