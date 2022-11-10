from src.controllers.controller import *
# from src.controllers.errors import *


routes = {
    "index": "/", 
    "index_page": IndexController.as_view("index"),
    "register": "/register",
    "register_page" : RegisterController.as_view("register"),
    # "not_found": 404, 
    # "not_found_controller": NotFoundController.as_view("not_found"),
}