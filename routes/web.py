from masonite.routes import Route

ROUTES = [
    Route.get("/", "CategoryController@index"),
    Route.get("/create", "CategoryController@create").name('category_create'),
    Route.post("/create", "CategoryController@store"),
    Route.get("/single/@id", "CategoryController@show").name("category_single"),
    Route.post("/update/@id", "CategoryController@update").name("category_update"),
    Route.get("/delete/@id", "CategoryController@destroy"),

    Route.group(
        [
            Route.get("/create", "TaskController@create").name("create"),
            Route.post("/create", "TaskController@store").name("store"),
            Route.get("/single/@id", "TaskController@show").name("single"),
            Route.post("/update/@id", "TaskController@update").name("update"),
            Route.get("/delete/@id", "TaskController@destroy").name("delete"),
            Route.get("/@category_id", "TaskController@index").name("list"),
        ],
        prefix="/task",
        name="task."
    )
]
