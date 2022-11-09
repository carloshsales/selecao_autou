from src.controllers.controller import *


routes = {
    "home": "/", 
    "hello": Controller.as_view("Hello")
}