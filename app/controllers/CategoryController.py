from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Category import Category


class CategoryController(Controller):
    def index(self, view: View):
        categories = Category.all()
        return view.render('category.list', {'categories': categories})

    def show(self, view: View, request: Request):
        category = Category.find_or_fail(request.param("id"))
        return view.render('category.single', {'category': category})

    def create(self, view: View):
        return view.render("category.create")

    def store(self, request: Request, response: Response):
        errors = request.validate({"name": "required"})
        if errors:
            return response.back()

        Category.create(name=request.input("name"))
        return response.redirect('/')

    def update(self, request: Request, response: Response):
        category = Category.find_or_fail(request.param("id"))

        errors = request.validate({"name": "required"})
        if errors:
            return response.redirect(name='category_single', params={"id": request.param("id")})

        category.name = request.input('name')
        category.save()
        return response.redirect('/')

    def destroy(self, request: Request, response: Response):
        post = Category.find_or_fail(request.param("id"))
        post.delete()
        return response.redirect('/')
