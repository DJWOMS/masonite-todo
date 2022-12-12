from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Category import Category
from app.models.Task import Task


class TaskController(Controller):
    def index(self, view: View, request: Request):
        tasks = Task.where("category_id", request.param("category_id")).get()
        return view.render("task.list", {"tasks": tasks})

    def create(self, view: View):
        categories = Category.all()
        return view.render("task.create", {"categories": categories})

    def store(self, request: Request, response: Response):
        error = request.validate(
            {
                "text": "required",
                "end_date": "required",
                "category_id": "required"
            }
        )
        if error:
            return response.redirect(name="task.create")

        Task.create(**request.only("text", "end_date", "category_id"))
        return response.redirect(
            name="task.list", params={"category_id": request.input("category_id")}
        )

    def show(self, view: View, request: Request):
        task = Task.find_or_fail(request.param("id"))
        categories = Category.all()
        return view.render('task.single', {"task": task, "categories": categories})

    def edit(self, view: View):
        return view.render("")

    def update(self, request: Request, response: Response):
        task = Task.find_or_fail(request.param("id"))

        errors = request.validate(
            {
                "text": "required",
                "end_date": "required",
                "category_id": "required"
            },
        )
        if errors:
            return response.redirect(name='task.single', params={"id": request.param("id")})

        data = request.only("text", "end_date", "category_id")
        data.update({"done": request.input("done", "off")})
        task.update(data)
        return response.redirect(
            name="task.list", params={"category_id": request.input("category_id")}
        )

    def destroy(self, request: Request, response: Response):
        Task.find_or_fail(request.param("id")).delete()
        return response.redirect(name="task.list")
