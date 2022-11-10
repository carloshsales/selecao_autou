from flask import Flask
from src.routes.route import routes


app = Flask(__name__)


app.add_url_rule(routes['index'],view_func=routes['index_page'])
app.add_url_rule(routes['register'],view_func=routes['register_page'])


# app.register_error_handler(routes['not_found'], routes['not_found_controller'])
