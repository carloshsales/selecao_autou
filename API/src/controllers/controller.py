from flask.views import MethodView


class Controller(MethodView):
    def get(self):
        return "HOME CONTROLLER"